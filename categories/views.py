from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

# permission and authentication classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import CategoriesPermissions

# filters
from .filters import CategoryFilters

# serializers
from .serializers import (
    ErrorMessageSerializer,
    SuccessMessageSerializer,
    CategoriesSerializer,
    CreateCategorySerializer,
)

# models
from .models import Category
from users.models import User
from businesses.models import Business

# utility functions
from .utility_func import jwt_authentication


'''
    => CATEGORY VIEWS SECTION
'''
class RetrieveCategoriesAPIView(APIView):
    permission_classes = [CategoriesPermissions, ]
    authentication_classes = [JWTAuthentication]
    filter_class = CategoryFilters


    def get(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        categories:list[Category] = Category.objects.filter(is_deleted=False)
        if not categories:
            return Response([], status=status.HTTP_200_OK)
        
        filtered_category = self.filter_class(request.query_params, queryset=categories).qs
        serializer = CategoriesSerializer(filtered_category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RetrieveCategoryAPIView(APIView):
    permission_classes = [CategoriesPermissions, ]
    authentication_classes = [JWTAuthentication]

    def get(self, request:Request, business_id:str, category_id:str, *args, **kwargs):
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
    permission_classes = [CategoriesPermissions, ]
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
    permission_classes = [CategoriesPermissions, ]
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
    permission_classes = [CategoriesPermissions, ]
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
    

'''
    => CATEGORY VIEWS SECTION BUSINESSES
'''

class RetrieveCategoriesByBusinessAPIView(APIView):
    permission_classes = [CategoriesPermissions, ]
    authentication_classes = [JWTAuthentication]

    def get(self, request:Request, business_id:str=None, *args, **kwargs):
        if not business_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        user:User = response
        business:Business = user.businesses.filter(id=business_id).first()
        if not business:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        categories:list[Category] = Category.objects.filter(business__id=business.id).filter(is_deleted=False)
        if not categories:
            return Response([], status=status.HTTP_200_OK)
        
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveCategoryByBusinessAPIView(APIView):
    permission_classes = [CategoriesPermissions, ]
    authentication_classes = [JWTAuthentication]

    def get(self, request:Request, category_id:str=None, business_id:str=None, *args, **kwargs):
        if not(category_id and business_id):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        user:User = response
        business:Business = user.businesses.filter(id=business_id).first()
        if not business:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            category:Category = Category.objects.get(id=category_id)
            if category.business.id != business.id:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if category.is_deleted:
                return Response(status=status.HTTP_404_NOT_FOUND)

        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = CategoriesSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
