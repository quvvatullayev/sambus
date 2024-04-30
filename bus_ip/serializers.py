from rest_framework import serializers
from .models import BusModel, BusStopModel

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusModel
        fields = '__all__'

class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStopModel
        fields = '__all__'