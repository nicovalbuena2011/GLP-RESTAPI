from django.contrib import admin
from . import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tipo',
        # 'nombre',
        'precio_unitario',
        'unidad_medida'
    )

admin.site.register(models.Producto, ProductAdmin)