from rest_framework import serializers
from .models import Buss, Bus, Route, Station

class BussSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buss
        fields = '__all__'

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


        