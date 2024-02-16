from django.contrib import admin
from . import models

# Register your models here.

class CustomersAdmin(admin.ModelAdmin):
    def get_model_fields(model):
        return [field.name for field in model._meta.fields]
    list_display = get_model_fields(models.Customers)

    search_fields = ('name',)

admin.site.register(models.Customers, CustomersAdmin)