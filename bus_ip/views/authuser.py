from rest_framework import generics
from django.contrib.auth.models import User
from ..serializers import UserSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS
# from ..forms import SignupForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth.models import User

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReadOnly(BasePermission):
    def has_object_permission(self, request:Request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user:User = request.user
        return user.is_staff == True

    

    