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
    sector = models.CharField(max_length = 200,default=None, help_text="Especificar que sector se encarga de pedir este insumo.")
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


class Remito(models.Model):
    ingresado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nro_remito = models.CharField(max_length = 100)
    fecha = models.DateField(auto_now=False)
    observaciones = models.CharField(max_length = 200)

    def __str__(self):
        r = self.nro_remito
        return r



class Entrada(models.Model):
    TIPO =(
        ('PROV','Proveedor'),
        ('PRES', 'Prestamo'),
        ('DEVO','Dev Prestamo')
    )

    ingresado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tipo = models.CharField(max_length = 4,choices=TIPO, default='PROV')
    remito = models.ForeignKey(Remito, on_delete=models.CASCADE,default=None, help_text="Dejar vacío si el artículo es la devolución de préstamo, o préstamo")
    articulo = models.ForeignKey(Lote_producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        r = "Item " + self.articulo + " de "  + self.remito
        return r

class Consumo_sector(models.Model):
    ingresado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha = fecha_ingreso = models.DateTimeField(default= timezone.now)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    observaciones = models.CharField(max_length = 200)
    
    def __str__(self):
        r = str(self.fecha)
        s = self.sector
        return r + s 



class Salida(models.Model):
    TIPO =(
        ('PROV','Proveedor'),
        ('PRES', 'Prestamo'),
        ('DEVO','Dev Prestamo')
    )
    tipo = models.CharField(max_length = 4,choices=TIPO,default='PROV')
    consumo_sector = models.ForeignKey(Consumo_sector, on_delete=models.CASCADE, default=None, help_text="Dejar vacio si se trata de un préstamo.")
    articulo = models.ForeignKey(Lote_producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        r = "Item " + self.articulo + " de "  + self.consumo_sector
        return r

class Laboratorio(models.Model):
    ingresado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 200)
    fecha_ingreso = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.nombre

    
class Prestamo_s(models.Model):
    #Para contabilizar los prestamos que hacemos o que devolvemos
    TIPO =(
        ('DEVS', 'Devolvemos')
        ('PRES', 'Prestamos'),
    )
    tipo = models.CharField(max_length = 4,choices=TIPO)
    fecha_prestamo = models.DateField(auto_now=False)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    destino = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    saliente = models.ForeignKey(Salida, on_delete=models.CASCADE)

    def __str__(self):
        r = self.tipo + " " + self.destino + " de "  + self.sector
        return r


class Prestamo_e(models.Model):
    #Para contabilizar los prestamos que nos hacen o devuelven.
    TIPO =(
        ('DEVN', 'Devuelven')
        ('PREN', 'Prestan'),
    )
    tipo = models.CharField(max_length = 4,choices=TIPO)
    fecha_prestamo = models.DateField(auto_now=False)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    destino = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    saliente = models.ForeignKey(Salida, on_delete=models.CASCADE)

    def __str__(self):
        r = self.tipo + " " + self.destino + " de "  + self.sector
        return r


