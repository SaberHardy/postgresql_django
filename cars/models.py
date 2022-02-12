from django.db import models


# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=30)
    license = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.DateField()
    vin = models.CharField(max_length=100)
    owner = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.make


