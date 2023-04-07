# simple jwt view
from django.http import HttpRequest
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# tokens
from rest_framework_simplejwt.tokens import RefreshToken

# permission and authentication classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, BaseAuthentication

# rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# serializers
from .serializers import (CustomTokenObtainPairSerializer, LoginRequestSerializer, LoginResponseSerializer, ErrorMessageSerializer)

# models
from .models import Token
from users.models import User

# types
from .base_types import LoginResponse, ErrorMessageResponse


# store token
def save_jwt_token(user:User, token):
    token_model:Token
    refresh_token = RefreshToken(token=token["refresh"])
    token_model, created_token = Token.objects.get_or_create(user=user)
    token_model.access_token = token["access"]
    token_model.refresh_token = token["refresh"]
    token_model.access_token_expiration = refresh_token.access_token.payload['exp']
    token_model.refresh_token_expiration = refresh_token.payload['exp']
    token_model.save()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomTokenRefreshView(TokenRefreshView):
    pass

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        serializer = LoginRequestSerializer(data=request.data)
        if serializer.is_valid() == False:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user:User = serializer.validated_data["user"]
        token_pair_view = CustomTokenObtainPairView.as_view()
        token_pair = token_pair_view(request._request)
        try:
            save_jwt_token(user=user, token=token_pair.data)
        except Exception as e:
            error_message = ErrorMessageResponse(message="couldn't save the user token", status_code=500)
            message_serializer = ErrorMessageSerializer(error_message)
            return Response(message_serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        token_data = LoginResponse(access_token=token_pair.data["access"], refresh_token=token_pair.data["refresh"],)
        response_serializer = LoginResponseSerializer(token_data)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

