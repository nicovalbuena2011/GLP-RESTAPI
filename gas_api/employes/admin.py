from django.contrib import admin
from . import models
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    def get_model_fields(model):
        return [field.name for field in model._meta.fields]
    list_display = get_model_fields(models.Empleado)

admin.site.register(models.Empleado, EmpleadoAdmin)