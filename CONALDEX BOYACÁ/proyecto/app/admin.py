from django.contrib import admin
from app.models import*
from .models import Categoria, Producto, Compra #agregue import para productos 
# Register your models here.
admin.site.register(Empleado)
admin.site.register(Ubicacion)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Compra)
admin.site.register(Producto)
admin.site.register(Normativa)
admin.site.register(Venta)
admin.site.register(Registro_venta)