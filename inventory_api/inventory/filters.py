import django_filters
from .models import InventoryItem


class InventoryItemFilter(django_filters.FilterSet):

    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    low_stock = django_filters.NumberFilter(
        field_name="quantity",
        lookup_expr='lte'
    )

    category = django_filters.CharFilter(
        field_name="category",
        lookup_expr='iexact'
    )

    class Meta:
        model = InventoryItem
        fields = ['category', 'min_price', 'max_price', 'low_stock']