from django.contrib import admin
from .models import Prov, Fabricante, Sector, tipo_Producto, Producto, Lote_producto, Remito, Consumo_sector,Salida,Prestamo_e,Prestamo_s, Entrada
# Register your models here.

admin.site.register(Prov)
admin.site.register(Fabricante)
admin.site.register(Sector)
admin.site.register(tipo_Producto)
admin.site.register(Producto)
admin.site.register(Lote_producto)
admin.site.register(Remito)
admin.site.register(Entrada)
admin.site.register(Salida)
admin.site.register(Consumo_sector)
admin.site.register(Prestamo_e)
admin.site.register(Prestamo_s)
