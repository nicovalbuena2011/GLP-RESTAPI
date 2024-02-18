from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from authentication.serializers import (
    UserSerializer
)
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["User"])
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the sistem"""
    serializer_class = UserSerializer

@extend_schema(tags=["User"])
class ManagerUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

