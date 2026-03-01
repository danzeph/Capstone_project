from django.contrib import admin
from inventory.models import InventoryChangeHistory, InventoryItem

admin.site.register(InventoryItem)
admin.site.register(InventoryChangeHistory)
