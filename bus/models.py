from django.db import models

# Create your models here.

class Buss(models.Model):
    busnumber = models.CharField(max_length=50)
    bussum = models.PositiveIntegerField(default=1)
    timelimte = models.TimeField()

    def __str__(self) -> str:
        return self.busnumber
    
class Bus(models.Model):
    driver = models.CharField(max_length=30)
    busid = models.CharField(max_length=30)
    img = models.ImageField(upload_to='./driverimg')
    bus = models.ForeignKey(Buss, on_delete=models.CASCADE)

    let = models.IntegerField()
    long = models.IntegerField()

    def __str__(self) -> str:
        return self.driver