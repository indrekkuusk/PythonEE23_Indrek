# moviesearch/urls.py
from django.urls import path
from .views import movie_search, movie_detail

urlpatterns = [
    path('search/', movie_search, name='movie_search'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),  # Add this line
]

