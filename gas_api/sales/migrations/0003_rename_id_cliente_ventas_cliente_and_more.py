# Generated by Django 4.2.7 on 2024-02-19 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20240218_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ventas',
            old_name='id_cliente',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='ventas',
            old_name='id_empleado',
            new_name='empleado',
        ),
        migrations.RenameField(
            model_name='ventas',
            old_name='id_producto',
            new_name='producto',
        ),
    ]
