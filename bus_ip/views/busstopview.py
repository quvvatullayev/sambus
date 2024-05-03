from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import BusStopSerializer, BusStopModel, BusModel, BusSerializer
from rest_framework.authentication import TokenAuthentication

class BusStopListView(generics.ListAPIView):
    queryset = BusStopModel.objects.all()
    serializer_class = BusStopSerializer
    # authentication_classes = [TokenAuthentication]

class BusStopCreateView(generics.CreateAPIView):
    queryset = BusStopModel.objects.all()
    serializer_class = BusStopSerializer
    authentication_classes = [TokenAuthentication]

class BusStopRetrieveView(generics.RetrieveAPIView):
    queryset = BusStopModel.objects.all()
    serializer_class = BusStopSerializer

    def retrieve(self, request, *args, **kwargs):

        busstop_obj = BusStopModel.objects.get(id = kwargs['pk'])
        busstop = BusStopSerializer(busstop_obj, many = False).data

        buss = []

        for pk in busstop['buss']:
            bus_obj = BusModel.objects.get(id = pk)
            bus = BusSerializer(bus_obj, many = False).data
            buss.append(bus)
        busstop['buss'] = buss
        return Response(data=busstop)

class BusStopUpdateView(generics.UpdateAPIView):
    queryset = BusStopModel.objects.all()
    serializer_class = BusStopSerializer
    authentication_classes = [TokenAuthentication]

class BusStopDestroyView(generics.DestroyAPIView):
    queryset = BusStopModel.objects.all()
    serializer_class = BusStopSerializer
    authentication_classes = [TokenAuthentication]