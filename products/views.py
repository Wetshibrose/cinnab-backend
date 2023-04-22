from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

# permission and authentication classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import ProductsPermissions

# serializers
from .serializers import (
    ProductsSerializer,
    CreateProductSerializer
)

# models
from .models import (
    Product,
    ProductImage,
    ProductVariant
)

# utility functions
from .utility_func import jwt_authentication

# filters
from .filters import ProductFilters


'''
    => PRODUCTS VIEWS SECTION
'''

class RetrieveProductsAPIView(APIView):
    permission_classes = [ProductsPermissions,]
    authentication_classes = [JWTAuthentication]
    filter_class = ProductFilters

    def get(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        products:list[Product] = Product.objects.filter(is_deleted=False)
        if not products:
            return Response([], status=status.HTTP_200_OK)
        
        filtered_products = self.filter_class(request.query_params, queryset=products).qs
        serializer = ProductsSerializer(filtered_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RetrieveProductAPIView(APIView):
    permission_classes = [ProductsPermissions,]
    authentication_classes = [JWTAuthentication]

    def get(self, request:Request, product_id:str, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        try:
            product:Product = Product.objects.get(id=product_id)
            if product.is_deleted:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = ProductsSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CreateProductAPIView(APIView):
    permission_classes = [ProductsPermissions,]
    authentication_classes = [JWTAuthentication]

    def post(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        serializer = CreateProductSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            new_product:Product = Product.objects.create(**serializer.validated_data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = ProductsSerializer(new_product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class EditProductAPIView(APIView):
    permission_classes = [ProductsPermissions,]
    authentication_classes = [JWTAuthentication]

    def post(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
    def put(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response    
        

class DeleteProductAPIView(APIView):
    permission_classes = [ProductsPermissions,]
    authentication_classes = [JWTAuthentication]

    def delete(self, request:Request, product_id:str, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        try:
            product:Product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        product.is_deleted = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

'''
    => PRODUCT IMAGE VIEWS SECTION
'''