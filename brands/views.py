from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

# permission and authentication classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import BrandsPermissions

# serializers
from .serializers import BrandsSerializer, CreateBrandSerializer

# models
from .models import Brand, BrandLogo
from users.models import User

# filters
from .filters import BrandFilters

# utility functions
from .utility_func import jwt_authentication

class RetrieveBrandsAPIView(APIView):
    permission_classes = [BrandsPermissions,]
    authentication_classes = [JWTAuthentication]
    filter_class = BrandFilters

    def get(self, request:Request, *args, **kwargs):
        brands:list[Brand] = Brand.objects.filter(is_deleted=False)
        if not brands:
            return Response([], status=status.HTTP_200_OK)
        
        filtered_brands = self.filter_class(request.query_params, queryset=brands).qs
        serializer = BrandsSerializer(filtered_brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RetrieveBrandAPIView(APIView):
    permission_classes = [BrandsPermissions,]
    authentication_classes = [JWTAuthentication]

    def get(self, request:Request, brand_id:str=None, *args, **kwargs):
        try:
            brand:Brand = Brand.objects.get(id=brand_id)
            if brand.is_deleted:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BrandsSerializer(brand)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateBrandAPIView(APIView):
    permission_classes = [BrandsPermissions,]
    authentication_classes = [JWTAuthentication]

    def post(self, request:Request, *args, **kwargs):
        serializer = CreateBrandSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class EditBrandAPIView(APIView):
    permission_classes = [BrandsPermissions, ]
    authentication_classes = [JWTAuthentication]
        
    def put(self, request:Request, brand_id:str=None, *args, **kwargs):
        if brand_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        brand:Brand =  Brand.objects.filter(is_deleted=False).filter(id=brand_id)
        serializer = CreateBrandSerializer(brand, data=request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def patch(self, request:Request, brand_id:str=None, *args, **kwargs):
        if brand_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        brand:Brand =  Brand.objects.filter(is_deleted=False).filter(id=brand_id)
        serializer = CreateBrandSerializer(brand, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)



class DeleteBrandAPIView(APIView):
    permission_classes = [BrandsPermissions, ]
    authentication_classes = [JWTAuthentication]

    def delete(self, request:Request, brand_id:str=None, *args, **kwargs):
        if brand_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        brand:Brand =  Brand.objects.filter(is_deleted=False).filter(id=brand_id)
        brand.is_deleted = True
        brand.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    