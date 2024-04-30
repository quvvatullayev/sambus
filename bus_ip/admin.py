from django.contrib import admin
from .models import BusModel, BusStopModel

admin.site.register([BusStopModel, BusModel])
