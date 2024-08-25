from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

# Your TMDB API key
TMDB_API_KEY = 'your_api_key_here'


def movie_detail(request, movie_id):
    # API URL to get movie details by ID
    movie_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&append_to_response=credits'

    response = requests.get(movie_url)
    movie = None

    if response.status_code == 200:
        movie = response.json()  # Get movie details including credits

    return render(request, 'moviedetails/detail.html', {'movie': movie})
