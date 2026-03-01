from django.shortcuts import render
from inventory.permissions import IsOwner
from inventory.models import InventoryItem, InventoryChangeHistory
from inventory.serializers import InventoryChangeHistorySerializer, InventoryItemSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


User = get_user_model()


class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
            'category': ['exact'],
            'price': ['exact', 'gte', 'lte'],
            'quantity': ['lte'],  # for low stock
        }

    search_fields = ['name','category']
    ordering_fields = ['name', 'quantity', 'price', 'date_added']

    def get_queryset(self):
        return InventoryItem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        old_quantity = instance.quantity
        new_instance = serializer.save()

        if old_quantity != new_instance.quantity:
            InventoryChangeHistory.objects.create(
                item=new_instance,
                changed_by=self.request.user,
                old_quantity=old_quantity,
                new_quantity=new_instance.quantity
            )


class InventoryHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InventoryChangeHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InventoryChangeHistory.objects.filter(
            item__owner=self.request.user
        ).order_by("-time_changed")
