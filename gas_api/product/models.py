from django.db import models

class Producto(models.Model):

    TIPO_CHOICES = [
        ('gas', 'Gas'),
        ('tanque_estacionario', 'Tanque Estacionario'),
        ('otro', 'Otro'),
    ]

    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nombre = models.CharField(max_length=100)  # Nombre del producto
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)  # Precio unitario del producto
    unidad_medida = models.CharField(max_length=50)  # Unidad de medida del producto (litros, kilogramos, etc.)

    def __str__(self):
        return self.nombre
