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
    UserSerializer, 
    CreateUserSerializer, 
    ErrorMessageSerializer, 
    SuccessMessageSerializer, 
    GenderTypeSerializer, 
    CreateGenderTypeSerializer,
    ProfilePictureSerializer,
    CreateProfilePictureSerializer,
)

# models
from .models import GenderType, User, ProfilePicture
from django.contrib.auth.models import Group

# class types
from .base_types import ErrorMessageResponse, SuccessMessageResponse

# utility functions
from .utility_func import make_username, jwt_authentication

# django
from django.contrib.auth.hashers import make_password

'''
    => USER VIEWS SECTION
'''
class RetrieveUsersAPIView(APIView):
    # permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
    def get(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response

        users:list[User] = User.objects.filter(is_deleted=False)
        if not users:
            return Response([], status=status.HTTP_200_OK)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RetrieveUserAPIView(APIView):
    # permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
    def get(self, request:Request, user_id, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        try:
            user:User = User.objects.get(id=user_id)
            if user.is_deleted:
                message = ErrorMessageResponse(success=False, error_message="User not found", status_code=404)
                serializer = ErrorMessageSerializer(message)
                return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateUserAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request:Request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        if not serializer.is_valid():
            message = ErrorMessageResponse(success=False, error_message="Json badly formatted", status_code=400)
            serializer = ErrorMessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        data:dict = serializer.validated_data
        try:
            role = Group.objects.get(id=data.get("role"))
        except Group.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            new_user:User = User.objects.create_user(
                phone_number=data["phone_number"],
                username= make_username(value=data["email"]),


                email = data.get("email"),
                gender = data.get("gender"),
                first_name = data.get("first_name"),
                last_name = data.get("last_name"),
                date_of_birth = datetime.strptime(data.get("date_of_birth"), "%Y-%m-%d").date() if data["date_of_birth"] else None,
                password=make_password(password=data.get("password"))
            )

            new_user.groups.add(role)
            new_user.save()

        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = UserSerializer(new_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EditUserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    
    def post(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response

    def put(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response


class DeleteUserAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def delete(self, request:Request, user_id, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        try:
            user:User | None = User.objects.filter(id=user_id)
        except User.DoesNotExist:
            message = ErrorMessageResponse(success=False, error_message="User not found", status_code=404)
            serializer = ErrorMessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        
        user.is_deleted = True
        user.save()

        message = SuccessMessageResponse(success=True, data={"message": "user successfully deleted"}, status_code=204)
        serializer = SuccessMessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        

'''
    => GENDER VIEWS SECTION
'''
class RetrieveGenderTypesAPIView(APIView):
    # permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    def get(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        genders:list = GenderType.objects.filter(is_deleted=False)
        if not genders:
            return Response([], status=status.HTTP_200_OK)

        serializer = GenderTypeSerializer(genders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RetrieveGenderTypeAPIView(APIView):
    # permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    def get(self, request:Request, gender_id, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        try:
            gender:GenderType | None = GenderType.objects.get(id=gender_id)
            if gender.is_deleted:
                message = ErrorMessageResponse(success=False, error_message="Gender Type doesn't exists.", status_code=404)
                serializer = ErrorMessageSerializer(message)
                return Response(status=status.HTTP_404_NOT_FOUND)
        except GenderType.DoesNotExist:
            message = ErrorMessageResponse(success=False, error_message="Gender Type doesn't exists.", status_code=404)
            serializer = ErrorMessageSerializer(message)
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = GenderTypeSerializer(gender)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateGenderTypeAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        serializer = CreateGenderTypeSerializer(data=request.data)
        if not serializer.is_valid():
            message = ErrorMessageResponse(success=False, error_message="Json badly formatted", status_code=400)
            serializer = ErrorMessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        data:dict = serializer.validated_data
        new_gender = GenderType.objects.create(
            name=data["name"],
        )
        new_gender.save()

        serializer = GenderTypeSerializer(new_gender)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class EditGenderTypeAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    
    def post(self, request:Request, *args, **kwargs):
        pass
    
    def put(self, request:Request, *args, **kwargs):
        pass

    
class DeleteGenderTypeAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def delete(self, request:Request, gender_id, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        try:
            gender:GenderType | None = GenderType.objects.filter(id=gender_id)
        except GenderType.DoesNotExist:
            message = ErrorMessageResponse(success=False, error_message="Gender Type not found", status_code=404)
            serializer = ErrorMessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        
        gender.is_deleted = True
        gender.save()

        message = SuccessMessageResponse(success=True, data={"message": "gender successfully deleted"}, status_code=204)
        serializer = SuccessMessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


'''
    => USER PROFILE PICTURE SECTION
'''

class RetrieveProfilePicturesAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        pictures:list = ProfilePicture.objects.filter(is_deleted=False)
        if not pictures:
            return Response([], status=status.HTTP_200_OK)

        serializer = ProfilePictureSerializer(pictures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RetrieveProfilePictureAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request:Request, picture_id, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        try:
            picture:ProfilePicture | None = ProfilePicture.objects.get(id=picture_id)
            if picture.is_deleted:
                message = ErrorMessageResponse(success=False, error_message="Profile picture doesn't exists.", status_code=404)
                serializer = ErrorMessageSerializer(message)
                return Response(status=status.HTTP_404_NOT_FOUND)
        except ProfilePicture.DoesNotExist:
            message = ErrorMessageResponse(success=False, error_message="Profile picture doesn't exists.", status_code=404)
            serializer = ErrorMessageSerializer(message)
            return Response(status=status.HTTP_404_NOT_FOUND)    
        
        serializer = ProfilePictureSerializer(picture)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateProfilePictureAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request:Request, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        user:User = response

        serializer = CreateProfilePictureSerializer(data=request.data)
        if not serializer.is_valid():
            message = ErrorMessageResponse(success=False, error_message="Json badly formatted", status_code=400)
            serializer = ErrorMessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        data:dict = serializer.validated_data
        new_picture = ProfilePicture.objects.create(
            url=data["url"],
            user=user
        )
        new_picture.save()

        serializer = ProfilePictureSerializer(new_picture)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class EditProfilePictureAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    
    def post(self, request:Request, *args, **kwargs):
        pass
    
    def put(self, request:Request, *args, **kwargs):
        pass

class DeleteProfilePictureAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def delete(self, request:Request, picture_id:str, *args, **kwargs):
        response = jwt_authentication(req=request)
        if response is Response:
            return response
        
        try:
            picture:ProfilePicture = ProfilePicture.objects.get(id=picture_id)
        except ProfilePicture.DoesNotExist:
            message = ErrorMessageResponse(success=False, error_message="Profile picture not found", status_code=404)
            serializer = ErrorMessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            message = ErrorMessageResponse(success=False, error_message=f"Something went wrong {e}", status_code=500)
            serializer = ErrorMessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        picture.is_deleted = True
        picture.save()

        message = SuccessMessageResponse(success=True, data={"message": "picture successfully deleted"}, status_code=204)
        serializer = SuccessMessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    
