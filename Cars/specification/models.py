from django.db import models

# Create your models here.

# specification/models.py

from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=128)
    year_built = models.IntegerField(default=2024)
    color = models.CharField(max_length=64)
    horsepower = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.year_built}) - {self.color}, {self.horsepower} HP"
