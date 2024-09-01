# moviedetails/urls.py
from django.urls import path
from .views import movie_detail_view

urlpatterns = [
    path('movie/<int:movie_id>/', movie_detail_view, name='movie_detail_view'),

]

