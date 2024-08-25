from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/save/', views.save_movie, name='save_movie'),
    path('bookmarked/', views.bookmarked_movies, name='bookmarked_movies'),
]

from django.urls import path
from . import views
