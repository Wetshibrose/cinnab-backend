from django_filters import rest_framework as filters

# models
from .models import Brand

class BrandFilters(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    is_published = filters.BooleanFilter(field_name="is_published")

    class Meta:
        model = Brand
        fields = (
            "name",
            "is_published",
        )
        