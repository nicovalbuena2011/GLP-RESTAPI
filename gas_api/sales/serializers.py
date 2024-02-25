from rest_framework import serializers
from .models import Ventas
from customers.models import Customers
from employes.models import Empleado
from product.models import Producto
from customers.serializers import CustomerSerializer
from employes.serializers import EmployeSerializer
from product.serializers import ProductSerializer

class VentasSerializer(serializers.ModelSerializer):
    metodo_pago_display = serializers.CharField(source='get_metodo_pago_display', read_only=True)
    cliente = CustomerSerializer()
    empleado = EmployeSerializer()
    producto = ProductSerializer()
    class Meta:
        model = Ventas
        fields = [
            'created_at',
            'modified',
            'cliente',
            'empleado',
            'producto',
            'total_venta_pesos',
            'total_venta_producto',
            'metodo_pago_display'
        ]

class CreateUpdateVentasSerializer(serializers.ModelSerializer):
    # Define los campos como PrimaryKeyRelatedField para recibir solo el número correspondiente
    cliente = serializers.PrimaryKeyRelatedField(queryset=Customers.objects.all())
    empleado = serializers.PrimaryKeyRelatedField(queryset=Empleado.objects.all())
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())
    class Meta:
        model = Ventas
        fields = [
            'cliente',
            'empleado',
            'producto',
            'total_venta_pesos',
            'total_venta_producto',
            'metodo_pago'
        ]

class VentaPesosProducto(serializers.Serializer):
    total_pesos = serializers.DecimalField(max_digits=20, decimal_places=3)
    total_producto = serializers.DecimalField(max_digits=20, decimal_places=3)