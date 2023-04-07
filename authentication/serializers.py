from rest_framework import serializers

from django.contrib.auth import authenticate

from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ErrorMessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    status_code = serializers.IntegerField()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = str(user.id)
        return token
    
class LoginRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        phone_number = data.get("phone_number")
        password = data.get("password")

        if phone_number and password:
            user  = authenticate(phone_number=phone_number, password=password)
            if user:
                if not user.is_active:
                    msg = _("User account is disabled.")
                    raise serializers.ValidationError(msg)
                data["user"] = user
            else:
                msg = _("Unable to log in with provided credentials")
                raise serializers.ValidationError(msg)
        else:
            msg = _("Must include 'username' and 'password'.")
            raise serializers.ValidationError(msg)
        
        return data

class LoginResponseSerializer(serializers.Serializer):
    acess_token = serializers.CharField()
    refresh_token = serializers.CharField()
