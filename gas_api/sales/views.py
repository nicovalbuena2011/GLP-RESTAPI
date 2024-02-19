from django.shortcuts import render
from .models import Ventas
from rest_framework import viewsets, authentication, permissions
from . import serializers
from drf_spectacular.utils import extend_schema
# Create your views here.
@extend_schema(tags=["Ventas"])
class VentasViewSet(viewsets.ModelViewSet):
    """
    A viewset for basic operations in sales models
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.VentasSerializer
    queryset = Ventas.objects.all()