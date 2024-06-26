from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializers import BusSerializer, BusModel
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny

class BusCreateView(generics.CreateAPIView):
    queryset = BusModel.objects.all()
    serializer_class = BusSerializer
    authentication_classes = [TokenAuthentication]

class BusListView(generics.ListAPIView):
    queryset = BusModel.objects.all()
    serializer_class = BusSerializer
    permission_classes = [AllowAny]

class BusRetrieveView(generics.RetrieveAPIView):
    queryset = BusModel.objects.all()
    serializer_class = BusSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the requested BusModel instance
        bus_stops:dict = instance.busstopmodel_set.all()  # Get all BusStopModel instances related to this BusModel
        serializer = self.get_serializer(instance)
        busstoplist = []
        for stop in bus_stops:
            data =  {
                'busstop_name':stop.busstop_name,
                'latitiude':stop.latitude,
                'longitude' : stop.longitude,
                'id_' :stop.id,
                }
            busstoplist.append(data)

        return Response({
            'bus': serializer.data,
            'bus_stops': [stop.busstop_name for stop in bus_stops],  # Serialize bus stops
            'bus_stops_data_all':busstoplist
        })
    
class BusUpdeteView(generics.UpdateAPIView):
    queryset = BusModel.objects.all()
    serializer_class = BusSerializer
    authentication_classes = [TokenAuthentication]

class BusDestroyView(generics.DestroyAPIView):
    queryset = BusModel.objects.all()
    serializer_class = BusSerializer
    authentication_classes = [TokenAuthentication]

