# Generated by Django 4.2.7 on 2024-02-15 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=80, verbose_name='Direccion')),
                ('telefono', models.CharField(max_length=15, verbose_name='Telefono')),
                ('tipo_cliente', models.CharField(choices=[('1', 'Empresa'), ('2', 'Persona natural'), ('3', 'Persona Juridica'), ('4', 'Restaurante')], max_length=20)),
            ],
        ),
    ]
