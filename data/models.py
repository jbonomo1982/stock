from django.db import models
from django.utils import timezone


class Prov(models.Model):
    ingresado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 200)
    fecha_ingreso = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.nombre

