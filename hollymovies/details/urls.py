# details/urls.py

from django.urls import path
from .views import myInformation, replacer

urlpatterns = [
    path('myinformation/', myInformation, name='myInformation'),

]

