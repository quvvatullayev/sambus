from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializer import Route, RouteSerializer

class RouteListCreateView(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class RouteDetilView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer