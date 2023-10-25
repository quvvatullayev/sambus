from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializer import Station, StationSerializer

class StationListCreateView(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class StationDetilView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer