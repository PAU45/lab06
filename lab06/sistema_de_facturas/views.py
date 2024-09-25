from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Factura, Cliente, Empleado, Producto, DetalleFactura
from django.db.models import Sum
from decimal import Decimal
from xhtml2pdf import pisa

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('crear_factura')
        else:
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'sistema_de_facturas/login.html', {'error': error_message})

    return render(request, 'sistema_de_facturas/login.html')

def admin_panel_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'sistema_de_facturas/admin_panel.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from decimal import Decimal
from .models import Factura, DetalleFactura, Producto, Cliente, Empleado

def crear_factura(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        empleado_id = request.POST.get('empleado')
        fecha = timezone.now().date()

        # Crear la factura
        factura = Factura(cliente_id=cliente_id, empleado_id=empleado_id, fecha=fecha)
        factura.save()

        # Procesar los productos seleccionados
        productos_ids = request.POST.getlist('productos')
        cantidades = request.POST.getlist('cantidades')

        total_general = Decimal(0)  # Inicializar total general

        for producto_id, cantidad in zip(productos_ids, cantidades):
            if cantidad:  # Asegúrate de que la cantidad no esté vacía
                cantidad = int(cantidad)  # Convierte a entero

                if producto_id and cantidad > 0:
                    producto = get_object_or_404(Producto, id_producto=producto_id)

                    # Asegúrate de que el precio unitario sea un Decimal
                    precio_unitario = Decimal(producto.precio_unitario)

                    subtotal = precio_unitario * Decimal(cantidad)
                    igv = subtotal * Decimal(0.18)
                    total = subtotal + igv

# Formatear para asegurarse de que tenga solo dos decimales
                    subtotal = subtotal.quantize(Decimal('0.01'))
                    igv = igv.quantize(Decimal('0.01'))
                    total = total.quantize(Decimal('0.01'))

                    # Crear detalle de la factura
                    detalle = DetalleFactura(
                        factura=factura,
                        producto=producto,
                        cantidad=cantidad,
                        subtotal=subtotal,
                        igv=igv,
                        total=total
                    )
                    detalle.save()

                    total_general += total  # Sumar el total a la factura

        # Guardar el total general en la factura si es necesario
        factura.total_general = total_general  # Asegúrate de que este campo exista en el modelo Factura
        factura.save()

        return redirect('factura_detalle', factura.numero)

    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    productos = Producto.objects.all()

    return render(request, 'crear_factura.html', {
        'clientes': clientes,
        'empleados': empleados,
        'productos': productos,
    })

def factura_detalle(request, numero):
    factura = get_object_or_404(Factura, numero=numero)
    detalles = factura.detalles.all()

    # Calcular el total general
    total_general = detalles.aggregate(total=Sum('total'))['total'] or Decimal(0)

    return render(request, 'factura_detalle.html', {
        'factura': factura,
        'detalles': detalles,
        'total_general': total_general,
    })

def factura_pdf(request, numero):
    factura = get_object_or_404(Factura, numero=numero)
    detalles = factura.detalles.all()
    total_general = detalles.aggregate(total=Sum('total'))['total'] or Decimal(0)

    # Renderizar la plantilla como HTML
    html_string = render_to_string('factura_detalle.html', {
        'factura': factura,
        'detalles': detalles,
        'total_general': total_general,
    })

    # Crear un PDF a partir del HTML
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{factura.numero}.pdf"'

    # Convertir HTML a PDF
    pisa_status = pisa.CreatePDF(html_string, dest=response)

    # Si hubo un error en la creación del PDF
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=400)

    return response

from sistema_de_facturas.models import Factura
factura = Factura.objects.first()
factura.detalles.all()