from rest_framework import serializers

# models
from .models import User, GenderType

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "phone_number", "gender", "date_of_birth", "bio", "first_name", "last_name")

class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True)
    gender_id = serializers.PrimaryKeyRelatedField(queryset=GenderType.objects.all(), required=True,)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=True)

    class Meta:
        model = User
        fields = ("email", "phone_number", "gender", "date_of_birth", "first_name", "last_name")
