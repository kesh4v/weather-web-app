from django.db import models

# Create your models here.
class TempHistory(models.Model):
    id = models.AutoField(primary_key=True)
    coordinate = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()