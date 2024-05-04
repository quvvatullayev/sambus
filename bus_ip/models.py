from django.db import models

class BusModel(models.Model):
    bus_name = models.CharField(max_length=30)
    time = models.IntegerField(default='1')

    def __str__(self) -> str:
        return self.bus_name
    
    class Meta:
        ordering = ["-id"]


class BusStopModel(models.Model):
    busstop_name = models.CharField(max_length=225)
    latitude = models.CharField(max_length=125)
    longitude = models.CharField(max_length=125)
    buss = models.ManyToManyField(BusModel, blank=True)

    def __str__(self) -> str:
        return self.busstop_name
    
    class Meta:
        ordering = ["-id"]

