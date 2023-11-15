from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializer import UserModel, UserSerializer
from django.contrib.gis.db.models import F, ExpressionWrapper, FloatField
from django.contrib.gis.measure import Distance
from django.db.models import Min
from bus.models import Bus, Station
from bus.serializer import StationSerializer
from rest_framework.views import APIView

class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserDetil(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
   
class UserFindNearestStation(APIView):
    def get(self, request:Request, pk):
        user_obj = UserModel.objects.get(id = pk)
        user:UserModel = UserSerializer(user_obj, many = False)

        user_location = user.location

        # Perform a spatial query to find the nearest bus station
        nearest_station_obj = Station.objects.annotate(
            distance=ExpressionWrapper(
                F('location').distance(user_location),
                output_field=FloatField()
            )
        ).order_by('distance').first()

        
        if nearest_station_obj:
            nearest_station = StationSerializer(nearest_station_obj, many = False)
            return Response(nearest_station.data)
            # Find the bus associated with the nearest station
            #     nearest_bus = Bus.objects.filter(my_bus_location=nearest_station).first()

            #     if nearest_bus:
            #         return nearest_bus
            #     else:
            #         return None
        else:
            return Response(data={'None':None})
