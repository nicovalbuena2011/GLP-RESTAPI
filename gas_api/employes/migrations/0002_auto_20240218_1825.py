# Generated by Django 3.2.24 on 2024-02-18 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='email',
            field=models.EmailField(max_length=40, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='estado',
            field=models.CharField(choices=[('1', 'Activo'), ('2', 'Inactivo')], max_length=20, verbose_name='Estado:'),
        ),
    ]
