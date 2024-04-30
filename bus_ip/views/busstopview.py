from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import BusStopSerializer, BusStopModel, BusModel, BusSerializer
from rest_framework.permissions import IsAdminUser
from .authuser import ReadOnly

class BusStopListCreateView(generics.ListCreateAPIView):
    queryset = BusStopModel.objects.all()
    serializer_class = BusStopSerializer
    permission_classes = [IsAdminUser|ReadOnly]

class BusStopRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusStopModel.objects.all()
    serializer_class = BusStopSerializer
    permission_classes = [IsAdminUser|ReadOnly]

    def retrieve(self, request, *args, **kwargs):

        busstop_obj = BusStopModel.objects.get(id = kwargs['pk'])
        busstop = BusStopSerializer(busstop_obj, many = False).data

        buss = []

        for pk in busstop['buss']:
            bus_obj = BusModel.objects.get(id = pk)
            bus = BusSerializer(bus_obj, many = False).data
            buss.append(bus)

        busstop['buss'] = buss

        # print(buss)
        # print(busstop)


        return Response(data=busstop)
