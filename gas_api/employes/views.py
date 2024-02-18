from django.shortcuts import render
from .models import Empleado
from rest_framework import viewsets, authentication, permissions
from . import serializers
from drf_spectacular.utils import extend_schema
# Create your views here.
@extend_schema(tags=["Empleado"])
class CustomersViewSet(viewsets.ModelViewSet):
    """
    A viewset for basic operations in customers models
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.EmployeSerializer
    queryset = Empleado.objects.all()