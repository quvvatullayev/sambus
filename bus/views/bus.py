from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializer import Buss, BussSerializer, Bus, BusSerializer

class BusListCreateView(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class BusDetilView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    