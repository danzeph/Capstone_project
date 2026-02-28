from rest_framework.routers import DefaultRouter
from .views import UserViewSet, InventoryItemViewSet, InventoryChangeLogViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'items', InventoryItemViewSet, basename='items')
router.register(r'changes', InventoryChangeLogViewSet, basename='changes')

urlpatterns = router.urls