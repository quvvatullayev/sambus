from django.db import models
from django.contrib.auth.models import User
from bus.models import Station

class UserModel(User):
    location = models.JSONField(blank=True, null=True)
    my_bus_location = models.ForeignKey(Station, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.username