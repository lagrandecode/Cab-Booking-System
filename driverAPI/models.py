from django.db import models

# Create your models here.
from django.db.models import DecimalField


class Driver(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    number = models.IntegerField(unique=True)
    license = models.CharField(max_length=80, unique=True)
    car_no = models.CharField(max_length=80, unique=True)


class DriverLocation(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    latitude = DecimalField(max_digits=9, decimal_places=6)
    longitude = DecimalField(max_digits=9, decimal_places=6)

