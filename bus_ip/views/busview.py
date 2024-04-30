from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import BusSerializer, BusModel
from rest_framework.permissions import IsAdminUser
from .authuser import ReadOnly

class BusListCreateView(generics.ListCreateAPIView):
    queryset = BusModel.objects.all()
    serializer_class = BusSerializer
    permission_classes = [IsAdminUser|ReadOnly]

class BusRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusModel.objects.all()
    serializer_class = BusSerializer
    permission_classes = [IsAdminUser|ReadOnly]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the requested BusModel instance
        bus_stops = instance.busstopmodel_set.all()  # Get all BusStopModel instances related to this BusModel
        serializer = self.get_serializer(instance)
        return Response({
            'bus': serializer.data,
            'bus_stops': [stop.busstop_name for stop in bus_stops]  # Serialize bus stops
        })

