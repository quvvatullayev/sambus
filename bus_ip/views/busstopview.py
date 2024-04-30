from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import BusStopSerializer, BusStopModel

class BusListCreateView(generics.ListCreateAPIView):
    queryset = BusStopModel.objects.all()
    serializer_class = BusStopSerializer

class BusRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusStopModel.objects.all()
    serializer_class = BusStopSerializer
