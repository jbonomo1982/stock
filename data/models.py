from django.db import models
from django.utils import timezone


class Prov(models.Model):
    ingresado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 200)
    fecha_ingreso = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.nombre

class Fabricante(models.Model):
    ingresado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 200)

    def __str__(self):
        return self.nombre


class Sector(models.Model):
    ingresado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    codigo = models.CharField(max_length = 10)
    descripcion = models.CharField(max_length = 200)

    def __str__(self):
        return self.codigo


class tipo_Producto(models.Model):
    ingresado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    codigo = models.CharField(max_length = 10)
    descripcion = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.codigo




class Producto(models.Model):
    ingresado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    codigo = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 200)
    tipo = models.ForeignKey(tipo_Producto, on_delete=models.CASCADE)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    observacion = models.CharField(max_length = 200)
    
    def __str__(self):
        r = self.descripcion
        return r

class Lote_producto(models.Model):
    ingresado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    codigo = models.CharField(max_length = 100)
    fecha_venc = models.DateField(auto_now=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
    observacion = models.CharField(max_length = 200)
    
    def __str__(self):
        r = self.codigo + " de " + self.producto
        return r

