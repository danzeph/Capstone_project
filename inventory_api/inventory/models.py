from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class InventoryItem(models.Model):
    """Inventoryitem model with owner field key as foreign"""
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="items")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



    

class InventoryChangeHistory(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name="history")
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    old_quantity = models.PositiveIntegerField()
    new_quantity = models.PositiveBigIntegerField()

    time_changed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} changed at {self.time_changed}"
