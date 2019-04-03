from django.contrib import admin
from .models import Prov, Fabricante, Sector, tipo_Producto, Producto, Lote_producto
# Register your models here.

admin.site.register(Prov)
admin.site.register(Fabricante)
admin.site.register(Sector)
admin.site.register(tipo_Producto)
admin.site.register(Producto)
admin.site.register(Lote_producto)
