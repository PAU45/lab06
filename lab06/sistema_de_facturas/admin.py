

# Register your models here.
from django.contrib import admin
from .models import Cliente, Empleado, Categoria, Producto, Factura, DetalleFactura, Usuario

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'ruc', 'direccion')
    search_fields = ('nombre', 'ruc')

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'email')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'descripcion', 'precio_unitario', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('descripcion',)

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cliente', 'empleado', 'fecha', 'cantidad')
    search_fields = ('numero',)
    list_filter = ('fecha',)

class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'subtotal', 'igv', 'total')
    search_fields = ('factura__numero',)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')

# Registra los modelos junto con sus configuraciones
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(DetalleFactura, DetalleFacturaAdmin)
admin.site.register(Usuario, UsuarioAdmin)