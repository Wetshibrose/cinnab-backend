# rest classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
# token classes
from rest_framework_simplejwt.tokens import AccessToken
# models
from users.models import User

# serializers
from .serializers import (
    ErrorMessageSerializer,
    SuccessMessageSerializer
)

# class types
from .base_types import ErrorMessageResponse, SuccessMessageResponse


def jwt_authentication(req: Request)->User|Response:
    auth_header:str = req.headers.get('Authorization')
    if not auth_header:
        message = ErrorMessageResponse(success=False, error_message="Token missing from header", status_code=400)
        serializer = ErrorMessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    token:str = auth_header.split(" ")[1].strip()
    try:
        auth_token = AccessToken(token)
        user_id:str = auth_token["user_id"]
    except Exception as e:
        message = ErrorMessageResponse(success=False, error_message="User not authenticated", status_code=401)
        serializer = ErrorMessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED)
    
    user:User = User.objects.get(id=user_id)
    if user.is_deleted:
        message = ErrorMessageResponse(success=False, error_message="User does not exist", status_code=400)
        serializer = ErrorMessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    return user
    