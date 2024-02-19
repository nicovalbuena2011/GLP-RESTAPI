from django.contrib import admin
from . import models
# Register your models here.


class GastosAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'descripcion',
        'monto'
    )


admin.site.register(models.Gastos, GastosAdmin)

class VentasAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'cliente',
        'empleado',
        'producto',
        'total_venta_pesos',
        'total_venta_producto',
        'metodo_pago'
    )
    # search_fields = ('created_at',)
    list_filter = ('metodo_pago',)

    date_hierarchy = 'created_at'  # Agrega la jerarquía de fechas para navegar por fechas más fácilmente

    def get_list_filter(self, request):
        # Agrega un filtro de rango de fechas personalizado
        default_list_filter = super().get_list_filter(request)
        custom_list_filter = list(default_list_filter)
        custom_list_filter.append(('created_at', admin.DateFieldListFilter))
        return custom_list_filter

admin.site.register(models.Ventas, VentasAdmin)
