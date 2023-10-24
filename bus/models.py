from django.db import models

# Create your models here.

class Buss(models.Model):
    busnumber = models.CharField(max_length=50)
    bussum = models.PositiveIntegerField(default=1)
    timelimte = models.TimeField()

    def __str__(self) -> str:
        return self.busnumber
    
    class Meta:
        ordering = ['-id']
    
class Bus(models.Model):
    driver = models.CharField(max_length=30)
    busid = models.CharField(max_length=30)
    img = models.ImageField(upload_to='./driverimg')
    bus = models.ForeignKey(Buss, on_delete=models.CASCADE)

    location = models.JSONField()

    def __str__(self) -> str:
        return self.driver
    
    class Meta:
        ordering = ['-id']
    
class Route(models.Model):
    buss = models.ForeignKey(Buss, on_delete=models.CASCADE)
    route = models.JSONField()

    def __str__(self) -> str:
        return self.buss.busnumber
    
    class Meta:
        ordering = ['-id']
    
class Station(models.Model):
    title = models.CharField(max_length=30)
    addresse = models.CharField(max_length=50)
    location = models.JSONField()
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-id']