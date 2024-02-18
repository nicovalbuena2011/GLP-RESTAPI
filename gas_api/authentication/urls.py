from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('token-auth/', obtain_auth_token, name = 'generate-token'),
    path('create/', views.CreateUserView.as_view(), name = 'create'),
    path('me/', views.ManagerUserView.as_view(), name = 'me')
]
