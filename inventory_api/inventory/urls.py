from rest_framework.routers import DefaultRouter
from inventory.views import InventoryViewSet, InventoryHistoryViewSet

router = DefaultRouter()

router.register(r'items', InventoryViewSet, basename='inventory')
router.register(r'history', InventoryHistoryViewSet, basename='history')

urlpatterns = router.urls