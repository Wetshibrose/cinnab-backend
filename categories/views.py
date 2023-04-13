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
    ErrorMessageSerializer,
    SuccessMessageSerializer,
    CategoriesSerializer,
    CreateCategorySerializer,
)

# models
from .models import Category

# class types
from .base_types import ErrorMessageResponse, SuccessMessageResponse

# utility functions
from .utility_func import jwt_authentication


'''
    => CATEGORY VIEWS SECTION
'''
class RetrieveCategoriesAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        categories:list[Category] = Category.objects.filter(is_deleted=False)
        if not categories:
            return Response([], status=status.HTTP_200_OK)
        
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RetrieveCategoryAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request:Request, category_id:str, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        try:
            category:Category = Category.objects.get(id=category_id)
            if category.is_deleted:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = CategoriesSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateCategoryAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        serializer = CreateCategorySerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EditCategoryAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
    def put(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response    
        
class DeleteCategoryAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def delete(self, request:Request, category_id:str, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        try:
            category:Category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        category.is_deleted = True
        category.save()
        return Response(status=status.HTTP_204_NO_CONTENT)