from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import BusSerializer, BusModel

class BusListCreateView(generics.ListCreateAPIView):
    queryset = BusModel.objects.all()
    serializer_class = BusSerializer

class BusRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusModel.objects.all()
    serializer_class = BusSerializer

