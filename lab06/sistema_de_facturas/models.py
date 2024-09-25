from django.db import models

class Cliente(models.Model):
    id_cliente = models.CharField(max_length=20, primary_key=True)  # Primary key manual
    nombre = models.CharField(max_length=100)
    ruc = models.CharField(max_length=11, unique=True)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)  # Campo para el apellido
    email = models.EmailField(max_length=100, unique=True)  # Campo de email, debe ser único

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_producto = models.CharField(max_length=20, primary_key=True)  # Primary key manual
    descripcion = models.CharField(max_length=200)
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.descripcion

class Factura(models.Model):
    numero = models.CharField(max_length=8, unique=True)  # Será autoincremental
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)  # Cambiado a PROTECT
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)  # Cambiado a PROTECT
    fecha = models.DateField()
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)  # Cambiado a PROTECT
    cantidad = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.numero:
            last_factura = Factura.objects.all().order_by('numero').last()
            if last_factura:
                # Incrementar el último número de factura, comenzando en 2000 si es el primero
                self.numero = str(int(last_factura.numero) + 1).zfill(8)
            else:
                self.numero = '00002000'  # Empezar en 2000
        super(Factura, self).save(*args, **kwargs)

    def __str__(self):
        return f'Factura {self.numero}'

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, related_name='detalles', on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    igv = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.descripcion}'

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)