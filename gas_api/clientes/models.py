from django.utils import timezone
from django.db import models

# Create your models here.


class Ventas(models.Model):
    created_at = models.DateTimeField( editable = False)
    modified = models.DateTimeField(editable = False)
    total_venta_pesos = models.FloatField('total venta en pesos: ')

    def save(self, *args, **kwargs):
        '''One save updated timestamps'''
        if not self.id:
            self.created_at = timezone.now()
        self.modified = timezone.now()
        return super(Ventas, self).save(*args, **kwargs)

    def __str__(self):
        return f'creado: {self.created_at} - editado: {self.modified} - valor: {self.total_venta_pesos}'