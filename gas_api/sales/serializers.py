from rest_framework import serializers
from .models import Ventas
from customers.serializers import CustomerSerializer
from employes.serializers import EmployeSerializer
from product.serializers import ProductSerializer

class VentasSerializer(serializers.ModelSerializer):
    cliente = CustomerSerializer()
    empleado = EmployeSerializer()
    producto = ProductSerializer()
    class Meta:
        model = Ventas
        fields = [
            'created_at',
            'modified',
            'total_venta_pesos',
            'cliente',
            'empleado',
            'producto',
            'total_venta_pesos',
            'total_venta_producto',
            'metodo_pago'
        ]