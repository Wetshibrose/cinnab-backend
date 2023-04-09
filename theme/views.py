from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

# permission and authentication classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

# serializers
from .serializers import (
    ThemeSerializer,
    CreateThemeSerializer,
    ErrorMessageSerializer,
    SuccessMessageSerializer,
)

# models
from .models import Theme

# utility functions
from .utility_func import jwt_authentication

# base class
from .base_types import (
    ErrorMessageResponse,
    SuccessMessageResponse
)

############################## Theme #####################################
class RetrieveThemesAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        themes:list[Theme] = Theme.objects.all()
        if not themes:
            return Response([], status=status.HTTP_200_OK)
        
        serializer = ThemeSerializer(themes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RetrieveThemeAPIView(APIView):
    # permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
    def get(self, request:Request, theme_id, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        try:
            theme:Theme = Theme.objects.get(id=theme_id)
            if theme.is_deleted:
                message = ErrorMessageResponse(success=False, error_message="Theme not found", status_code=404)
                serializer = ErrorMessageSerializer(message)
                return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        except Theme.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ThemeSerializer(theme)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateUserAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request:Request, *args, **kwargs):
        serializer = CreateThemeSerializer(data=request.data)
        if not serializer.is_valid():
            message = ErrorMessageResponse(success=False, error_message="Json badly formatted", status_code=400)
            serializer = ErrorMessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        data:dict = serializer.validated_data
        new_theme:Theme = Theme.objects.create(
            primary_color=data["primary_color"]
        )
        new_theme.save()

        serializer = ThemeSerializer(new_theme)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EditUserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    
    def post(self, request:Request, *args, **kwargs):
        pass

    def put(self, request:Request, *args, **kwargs):
        pass

    def patch(elf, request:Request, *args, **kwargs):
        pass



class DeleteUserAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def delete(self, request:Request, theme_id, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        try:
            theme:Theme|None = Theme.objects.filter(id=theme_id)
        except Theme.DoesNotExist:
            message = ErrorMessageResponse(success=False, error_message="Theme not found", status_code=404)
            serializer = ErrorMessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        
        theme.is_deleted = True
        theme.save()

        message = SuccessMessageResponse(success=True, data={"message": "theme successfully deleted"}, status_code=204)
        serializer = SuccessMessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        
