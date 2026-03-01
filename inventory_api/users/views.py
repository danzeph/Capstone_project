from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        """Users can only access their own account; admin sees everyone"""
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        if user.is_authenticated:
            return User.objects.filter(id=user.id)
        return User.objects.none()
    
    def get_permissions(self):
        """Allow anyone to register"""
        if self.action == 'create':
            return [permissions.AllowAny()]
    
        return [permissions.IsAuthenticated()]

