# specification/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('color/<str:color>/', views.get_cars_by_color, name='get_cars_by_color'),
    path('name/<str:name>/', views.get_cars_by_name, name='get_cars_by_name'),
    path('horsepower/<int:horsepowermin>/<int:horsepowermax>/', views.get_cars_by_horsepower, name='get_cars_by_horsepower'),
]
exit