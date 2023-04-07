from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# permission and authentication classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, BaseAuthentication

# serializers
from .serializers import UserSerializer, CreateUserSerializer

# models
from .models import GenderType, User


class RetrieveUsersAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        users:list[User] = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
class RetrieveUserAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, user_id, *args, **kwargs):
        try:
            user:User = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

class CreateUserAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class EditUserAPIView(APIView):
    pass

class DeleteUserAPIView(APIView):
    pass

