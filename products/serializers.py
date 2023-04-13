from rest_framework import serializers

# models
from .models import (
    Product,
    ProductImage,
    ProductVariant
)

from categories.models import Category

class ErrorMessageSerializer(serializers.Serializer):
    success = serializers.BooleanField(required=True)
    error_message = serializers.CharField(required=True)
    status_code = serializers.IntegerField(required=True)

class SuccessMessageSerializer(serializers.Serializer):
    success = serializers.BooleanField(required=True)
    data = serializers.DictField(required=True)
    status_code = serializers.IntegerField(required=True)

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "selling_price",
            "stock_quantity",
            "is_tracking",
            "is_active",
            "date_created"
        )

class CreateProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    selling_price = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)
    buying_price = serializers.DecimalField(required=False, allow_null=True, max_digits=10, decimal_places=2)
    stock_quantity = serializers.IntegerField(required=False, allow_null=True)
    barcode = serializers.CharField(required=False, allow_null=True)
    weight = serializers.DecimalField(required=False, allow_null=True, max_digits=10, decimal_places=2)
    length = serializers.DecimalField(required=False, allow_null=True, max_digits=10, decimal_places=2)
    height = serializers.DecimalField(required=False, allow_null=True, max_digits=10, decimal_places=2)
    rating = serializers.DecimalField(required=False, allow_null=True, max_digits=3, decimal_places=2)
    discount_price = serializers.DecimalField(required=False, allow_null=True, max_digits=10, decimal_places=2)
    color = serializers.CharField(required=False, allow_null=True)
    is_tracking = serializers.BooleanField(required=False, allow_null=True)
    is_active = serializers.BooleanField(required=False, allow_null=True)
    mnf_date = serializers.DateField(required=False, allow_null=True)
    exp_date = serializers.DateField(required=False, allow_null=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.filter(is_deleted=False),
        required=False,
        allow_null=True
    )
    # brand = serializers.PrimaryKeyRelatedField(
    #     queryset = Promotion.objects.filter(is_deleted=True),
    #     required=False,
    #     allow_null=True
    # )
    # promotion = serializers.PrimaryKeyRelatedField(
    #     queryset = Promotion.objects.filter(is_deleted=False),
    #     required=False,
    #     allow_null=True
    # )
    # sku = serializers.PrimaryKeyRelatedField(
    #     queryset = Unit.objects.filter(is_deleted=False),
    #     required=True,
    # )
    # manufacturer = serializers.PrimaryKeyRelatedField(
    #     queryset = Manufacturer.objects.filter(is_deleted=False)
    #     required=False,
    #     allow_null=True
    # )
    # supplier = serializers.PrimaryKeyRelatedField(
    #     queryset = Supplier.objects.filter(is_deleted=False)
    #     required=False,
    #     allow_null=True
    # )
    # tax = serializers.PrimaryKeyRelatedField(
    #     queryset = Tax.objects.filter(is_deleted=False),
    #     required=True,
    # )
    # business = serializers.PrimaryKeyRelatedField(
    #     queryset = Business.objects.filter(is_deleted=False),
    #     required=True,
    # )


    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "selling_price",
            "buying_price",
            "stock_quantity",
            "barcode",
            "weight",
            "length",
            "height",
            "rating",
            "discount_price",
            "color",
            "is_tracking",
            "is_active",
            # "promotion",
            "mnf_date",
            "exp_date",
            "category",
            "date_created"
        )
        read_only_fields = ("id", "date_created")

        