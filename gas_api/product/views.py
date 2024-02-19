from django.shortcuts import render
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
# Create your views here.
from .serializers import ProductSerializer
from .models import Producto
from drf_spectacular.utils import extend_schema
# Create your views here.
@extend_schema(tags=["Product"])

class RetrieveUpdateProduct(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Producto.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
