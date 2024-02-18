from rest_framework import serializers
from .models import Empleado
class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

    def validate_cedula(self, value):
        """Validate that the cedula field is unique"""
        if value is None or value == '':
            raise serializers.ValidationError('El campo de cedula  es requerido')
        if Empleado.objects.filter(cedula = value).exists():
            raise serializers.ValidationError('Este numero de cedula ya esta asociado a un empleado')
        
        return value