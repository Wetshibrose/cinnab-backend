from rest_framework import serializers

# models
from .models import User, GenderType, ProfilePicture
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "phone_number", "gender", "date_of_birth", "bio", "first_name", "last_name")

class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True)
    gender = serializers.PrimaryKeyRelatedField(queryset=GenderType.objects.all(), required=True,)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(allow_null=True)
    password = serializers.CharField(required=True)
    role = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        required=True,
    )


class ErrorMessageSerializer(serializers.Serializer):
    success = serializers.BooleanField(required=True)
    error_message = serializers.CharField(required=True)
    status_code = serializers.IntegerField(required=True)

class SuccessMessageSerializer(serializers.Serializer):
    success = serializers.BooleanField(required=True)
    data = serializers.DictField(required=True)
    status_code = serializers.IntegerField(required=True)

class GenderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderType
        fields = ("id", "name")

class CreateGenderTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model = GenderType
        fields = ("name",)


class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = ("id", "url", "user")

class CreateProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = ("url",)