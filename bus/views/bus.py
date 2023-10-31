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

    def retrieve(self, request, *args, **kwargs):
        bus_obj = Bus.objects.get(id = kwargs['pk'])
        bus = BusSerializer(bus_obj, many = True).data

        buss_obj = Buss.objects.get(id = bus['id'])
        buss = BussSerializer(buss_obj, many = False).data

        data = {
            'bus':bus,
            'buss':buss
        }
        
        return Response(data=data)
    