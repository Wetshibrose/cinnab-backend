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
        fields = ("id", "name", "description", "parent", "related_categories")

class CreateCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False, allow_null=True)
    meta_keywords = serializers.CharField(required=False, allow_null=True)
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(is_deleted=False),
        required=False,
        allow_null=True
    )
    related_categories = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.filter(is_deleted=False),
        many=True,
        required=False,
        allow_null=True
    )
     
    class Meta:
        model = Category
        fields = ("id", "name", "description", "meta_keywords", "parent", "related_categories", "is_active", "is_featured")
        read_only_fields = ("id",)
    
    def create(self, validated_data):
        related_categories = validated_data.pop("related_categories", [])
        new_category:Category = Category.objects.create(**validated_data)
        new_category.related_categories.set(related_categories)

        data = super().to_representation(new_category)
        return data

    def update(self, instance, validated_data):
        related_categories = validated_data.pop("related_categories", [])
        new_category:Category = super().update(instance, validated_data)
        new_category.related_categories.set(related_categories)
        return new_category