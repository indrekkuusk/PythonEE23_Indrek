from django.shortcuts import render

# Create your views here.

# specification/views.py

from django.http import JsonResponse
from .models import Car

def get_cars_by_color(request, color):
    cars = Car.objects.filter(color=color)
    data = list(cars.values())
    return JsonResponse(data, safe=False)

def get_cars_by_name(request, name):
    cars = Car.objects.filter(name=name)
    data = list(cars.values())
    return JsonResponse(data, safe=False)

def get_cars_by_horsepower(request, horsepowermin, horsepowermax):
    cars = Car.objects.filter(horsepower__gte=horsepowermin, horsepower__lte=horsepowermax)
    data = list(cars.values())
    return JsonResponse(data, safe=False)
