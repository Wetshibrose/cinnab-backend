from rest_framework import serializers

# django
from django.utils.text import slugify

# models
from .models import Category

class ErrorMessageSerializer(serializers.Serializer):
    success = serializers.BooleanField(required=True)
    error_message = serializers.CharField(required=True)
    status_code = serializers.IntegerField(required=True)

class SuccessMessageSerializer(serializers.Serializer):
    success = serializers.BooleanField(required=True)
    data = serializers.DictField(required=True)
    status_code = serializers.IntegerField(required=True)

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "slug", "description", "parent", "related_categories")

class CreateCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False, allow_null=True)
    meta_keyword = serializers.CharField(required=False, allow_null=True)
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(is_deleted=False),
        required=False,
        allow_null=True
    )
    related_categories = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.filter(is_deleted=False),
        many=True,
        required=False,
        allow_nul=True
    )
     
    class Meta:
        model = Category
        fields = ("name", "description", "meta_keywords", "parent", "related_categories", "is_active", "is_featured")

    
    def create(self, validated_data):
        related_categories = validated_data.pop("related_categories", [])
        new_category:Category = Category.objects.create(**validated_data)
        new_category.related_categories.set(related_categories)
        return new_category

    def update(self, instance, validated_data):
        related_categories = validated_data.pop("related_categories", [])
        new_category:Category = super().update(instance, validated_data)
        new_category.related_categories.set(related_categories)
        return new_category