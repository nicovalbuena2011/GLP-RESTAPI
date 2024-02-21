from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.VentasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('filter-ventas', views.VentasPorPeriodoDeTiempoAPI.as_view(), name = 'ventas_filtradas')
]