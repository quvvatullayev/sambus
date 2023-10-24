from django.db import models

# Create your models here.

class Bus(models.Model):
    busnumber = models.CharField(max_length=50)
    bussum = models.PositiveIntegerField(default=1)
    timelimte = models.TimeField()

    def __str__(self) -> str:
        return self.busnumber