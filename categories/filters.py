# django filter
from django_filters import rest_framework as filters


# models
from .models import Category

class CategoryFilters(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    meta_keywords = filters.CharFilter(field_name="meta_keywords", lookup_expr="icontains")
    business = filters.NumberFilter(field_name="business__id", )
    is_active = filters.BooleanFilter(field_name="is_active")
    is_featured = filters.BooleanFilter(field_name="is_featured")

    class Meta:
        model = Category
        fields = (
            "name",
            "meta_keywords",
            "business",
            "is_active",
            "is_featured"
        )