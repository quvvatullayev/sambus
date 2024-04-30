from rest_framework import serializers
from .models import BusModel, BusStopModel
from django.contrib.auth.models import User

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusModel
        fields = '__all__'

class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStopModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'