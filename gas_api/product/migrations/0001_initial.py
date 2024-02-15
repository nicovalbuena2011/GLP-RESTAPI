# Generated by Django 4.2.7 on 2024-02-15 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('gas', 'Gas'), ('tanque_estacionario', 'Tanque Estacionario'), ('otro', 'Otro')], max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unidad_medida', models.CharField(max_length=50)),
            ],
        ),
    ]
