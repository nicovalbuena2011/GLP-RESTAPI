from django.shortcuts import render
from .models import Ventas
from rest_framework import viewsets, authentication, permissions
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
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

class VentasPorPeriodoDeTiempoAPI(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        fecha_inicio = self.request.query_params.get('fecha_inicio')
        fecha_fin = self.request.query_params.get('fecha_fin')
        # print(f'Fecha de inicio: {fecha_inicio}')
        # print(f'Fecha de fin: {fecha_fin}')
        # Filtrar las ventas por las fechas proporcionadas
        ventas = Ventas.objects.filter(created_at__range=[fecha_inicio, fecha_fin])
        
        # Serializar los datos filtrados
        serializer = serializers.VentasSerializer(ventas, many=True)
        
        return Response(serializer.data)