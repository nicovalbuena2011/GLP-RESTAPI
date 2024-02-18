from django.db import models

# Create your models here.


class Empleado(models.Model):

    estado_empleado = [
        ('1','Activo'),
        ('2','Inactivo')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length = 20, blank = False)
    last_name = models.CharField('Apellidos', max_length = 30, blank = False)
    telefono = models.CharField('Telefono', max_length = 20, blank = False)
    email = models.EmailField('Email', max_length = 40)
    cedula = models.CharField('Cedula', max_length = 20)
    estado = models.CharField('Estado:',max_length=20, choices = estado_empleado)

    def __str__(self):
        return f'{self.name} {self.last_name} - Cedula: {self.cedula}'

    
