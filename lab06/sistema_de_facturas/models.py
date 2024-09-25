from django.db import models

class Trabajador(models.Model):
    nombre = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre =  models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    ruc = models.CharField(max_length=11)
    guia_remision = models.CharField(max_length=50)

class Detalle_factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField('fecha detalle')

class Factura(models.Model):
    detalle = models.ForeignKey(Detalle_factura, on_delete=models.CASCADE)
    igv = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)