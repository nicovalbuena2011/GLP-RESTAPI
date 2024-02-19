from rest_framework import serializers
from .models import Producto 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['tipo', 'precio_unitario', 'unidad_medida']
        