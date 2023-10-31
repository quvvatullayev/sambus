from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializer import UserModel, UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserDetil(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer