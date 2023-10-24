from django.contrib import admin

# Register your models here.

from .models import Bus, Buss, Route, Station
from django.contrib.auth.models import Group

admin.site.unregister([Group])
admin.site.register([Buss, Bus, Route, Station])
