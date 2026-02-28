from rest_framework import viewsets, permissions, filters
from .models import InventoryItem
from .serializers import InventoryChangeLogSerializer, InventoryItemSerializer, InventoryChangeLog, UserSerializer
from .permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objets.all()
    serializer_class = UserSerializer


class InventoryItemViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name']
    ordering_fields = ['name', 'quantity', 'price', 'date_added']

    def get_queryset(self):
        return InventoryItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        old_quantity = self.get_object().quantity
        instance = serializer.save()

        if old_quantity != instance.quantity:
            InventoryChangeLog.objects.create(
                item=instance,
                changed_by=self.request.user,
                old_quantity=old_quantity,
                new_quantity=instance.quantity
            )


class InventoryChangeLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InventoryChangeLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InventoryChangeLog.objects.filter(
            item__user=self.request.user
        )