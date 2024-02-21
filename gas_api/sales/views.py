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
    queryset = Ventas.objects.all()
    serializer_class = serializers.CreateUpdateVentasSerializer
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.VentasSerializer
        return serializers.CreateUpdateVentasSerializer