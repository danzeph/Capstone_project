from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)


class InventoryItem(models.Model):
    """Inventory item Model with user as a foreign key"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='items')
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='items')

    # ordering = ['-date_added']
    def __str__(self):
        return f"{self.name} - Category: {self.category}"


class InventoryChangeLog(models.Model):
    """
    Iventory_change log model for logging changes with an item
    fields: 
        item - get's model deleted upon deletion of an item
        user - sets to null upon deletion of item to keep log safe
    """
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='changes')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    old_quantity = models.PositiveIntegerField()
    new_quantity = models.PositiveIntegerField()
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} changed on {self.changed_at}"
