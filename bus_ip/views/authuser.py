from rest_framework import generics
from django.contrib.auth.models import User
from ..serializers import UserSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class Login_user(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request:Request):
        username:User = request.user
        
        if User.objects.filter(username = username):
            user = User.objects.get(username = username)
            token, uniq = Token.objects.get_or_create(user = user)
            return Response({"token":token.key})
        else:
            return Response({"user":"user not found"})

class Logout_user(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request:Request):
        username:User = request.user
        user = User.objects.get(username = username)

        if Token.objects.get(user=user):
            token = Token.objects.get(user = user)
            token.delete()
            return Response({"user":"user's token is deleted Successfully"})
        else:
            return Response({"user":"user not found"})

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDestroyView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReadOnly(BasePermission):
    def has_object_permission(self, request:Request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user:User = request.user
        return user.is_staff == True

    

    