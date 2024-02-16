from django.db import models

# Create your models here.

class Customers(models.Model):

    client_choices = [
        ('1','Empresa'),
        ('2','Persona natural'),
        ('3','Persona Juridica'),
        ('4','Restaurante'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length = 50)
    direccion = models.CharField('Direccion', max_length = 80)
    telefono = models.CharField('Telefono', max_length = 15)
    tipo_cliente = models.CharField(choices = client_choices, max_length = 20)
    email = models.EmailField('email', max_length = 30,default = 'prueba@prueba.com')

    class Meta:
        verbose_name_plural = 'Lista de Clientes'

    def __str__(self):
        return f'{self.name} - Direccion: {self.direccion} - Telefono: {self.telefono}'
