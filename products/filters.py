# django filter
from django_filters import rest_framework as filters

# models
from .models import Product


class ProductFilters(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    selling_price = filters.NumericRangeFilter(field_name="selling_price")
    discount_price = filters.NumberFilter(field_name="discount_price", lookup_expr="gte")
    rating = filters.NumberFilter(field_name="rating")
    category = filters.NumberFilter(field_name="category__id")
    color = filters.CharFilter(field_name="color")
    stock_quantity = filters.NumberFilter(field_name="stock_quantity", lookup_expr="gte")
    # brand = filters.NumberFilter(field_name="brand__id")

    class Meta:
        model = Product
        fields = (
            "name", 
            "selling_price",
            "discount_price",
            "rating",
            "category",
            "color",
            "stock_quantity"
        )