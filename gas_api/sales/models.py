from django.utils import timezone
from django.db import models

from customers.models import Customers
from employes.models import Empleado
from product.models import Producto

# Create your models here.


class Ventas(models.Model):

    PAGO_CHOICES = [
        ('Efectivo', 'Efectivo'),
        ('Transferencia Bancaria', 'Transferencia Bancaria'),
        ('NEQUI', 'NEQUI'),
        ('Daviplata', 'Daviplata'),
        ('Otro', 'Otro'),
    ]

    created_at = models.DateField( editable = False)
    modified = models.DateTimeField(editable = False)
    total_venta_pesos = models.FloatField('total venta en pesos: ')
    id_cliente = models.ForeignKey(Customers, on_delete = models.CASCADE)
    id_empleado = models.ForeignKey(Empleado, on_delete = models.SET_NULL, null = True)
    id_producto = models.ForeignKey(Producto, on_delete = models.PROTECT)
    total_venta_pesos = models.DecimalField(max_digits=20, decimal_places=2)
    total_venta_producto = models.DecimalField(max_digits=20, decimal_places=2)
    metodo_pago = models.CharField('metodo de pago', choices = PAGO_CHOICES,max_length=50)

    def save(self, *args, **kwargs):
        '''One save updated timestamps'''
        if not self.id:
            self.created_at = timezone.now()
        self.modified = timezone.now()
        return super(Ventas, self).save(*args, **kwargs)

    def __str__(self):
        return f'creado: {self.created_at} - editado: {self.modified} - valor: {self.total_venta_pesos}'
    
class Gastos(models.Model):
    created_at = models.DateField( editable = True )
    descripcion = models.TextField('Descripcion', max_length = 100)
    monto = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f'{self.descripcion} -- {self.monto}'