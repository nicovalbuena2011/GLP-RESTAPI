from django.shortcuts import render
from .models import Ventas
from django.db.models import Q
from rest_framework import viewsets, authentication, permissions, status
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
    
@extend_schema(tags=["Ventas"])
class VentasPorPeriodoDeTiempoAPI(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')
        metodo_pago = request.query_params.get('metodo_pago')
        nombre_cliente = request.query_params.get('nombre_cliente')
        
        # Inicializar una consulta base que devuelve todas las ventas
        query = Q()
        
        # Agregar filtro por fechas si están presentes
        if fecha_inicio and fecha_fin:
            query &= Q(created_at__range=[fecha_inicio, fecha_fin])
        
        # Agregar filtro por método de pago si está presente
        if metodo_pago:
            query &= Q(metodo_pago=metodo_pago)

        # Agregar filtro por nombre del cliente si está presente
        if nombre_cliente:
            # Realizar búsqueda insensible a mayúsculas/minúsculas
            query &= Q(cliente__name__icontains=nombre_cliente)
        
        # Filtrar las ventas según la consulta construida
        ventas = Ventas.objects.filter(query)

        # Comprobar si se encontraron registros
        if not ventas.exists():
            return Response({"message": "No se encontraron ventas"}, status=status.HTTP_404_NOT_FOUND)
        
        
        # Serializar los datos filtrados
        serializer = serializers.VentasSerializer(ventas, many=True)
        
        return Response(serializer.data)