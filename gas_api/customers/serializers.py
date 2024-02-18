from rest_framework import serializers
from .models import Customers
class CustomerSerializer(serializers.ModelSerializer):
    tipo_cliente_display = serializers.CharField(source='get_tipo_cliente_display', read_only=True)

    class Meta:
        model = Customers
        fields = ['id', 'name', 'direccion', 'telefono', 'tipo_cliente', 'tipo_cliente_display', 'email']

    def validate_email(self, value):
        """Validate that the email field is an adress and is unique"""
        if value is None or value == '':
            raise serializers.ValidationError('El campo de correo electronico es requerido')
        if Customers.objects.filter(email = value).exists():
            raise serializers.ValidationError('Este correo electronico ya esta en uso por otro cliente')
        
        return value