from rest_framework import serializers
from .models import Buss, Bus, Route, Station

class BussSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buss
        fields = '__all__'