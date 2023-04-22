from rest_framework import serializers

# models
from .models import Brand, BrandLogo

class ErrorMessageSerializer(serializers.Serializer):
    success = serializers.BooleanField(required=True)
    error_message = serializers.CharField(required=True)
    status_code = serializers.IntegerField(required=True)

class SuccessMessageSerializer(serializers.Serializer):
    success = serializers.BooleanField(required=True)
    data = serializers.DictField(required=True)
    status_code = serializers.IntegerField(required=True)


class BrandsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "description",
            "is_published"
        )

class CreateBrandSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False, allow_null=True)
    business = serializers.PrimaryKeyRelatedField(
        queryset = Brand.objects.filter(is_deleted=False),
        many=True,
        required=False,
        allow_null=True
    )
    is_published = serializers.BooleanField(required=False)

    class Meta:
        model = Brand
        fields = (
            "id",
            "name",
            "description",
            "business",
            "is_published"
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        businesses = validated_data.pop("business", [])
        new_brand:Brand = Brand.objects.create(**validated_data)
        new_brand.business.set(businesses)

        data = super().to_representation(new_brand)
        return data
    
    def update(self, instance, validated_data):
        businesses = validated_data.pop("business", [])
        new_brand:Brand = super().update(instance, validated_data)
        new_brand.business.set(businesses)

        return new_brand
    
