from django.db import models
# Create your models here.
from django.db.models import OneToOneField


class Temp(models.Model):
    time = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)

class Light(models.Model):
    status = models.CharField(max_length=100)
    lux = models.CharField(max_length=100)

class Humidity(models.Model):
    level = models.CharField(max_length=100)


#image = models.FilePathField(path="/img")