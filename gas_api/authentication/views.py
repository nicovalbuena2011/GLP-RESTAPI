from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from authentication.serializers import (
    UserSerializer
)

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the sistem"""
    serializer_class = UserSerializer

class ManagerUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

