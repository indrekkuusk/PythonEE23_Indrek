from django.shortcuts import render

# Create your views here.

import requests
from django.shortcuts import render
from .forms import MovieSearchForm

# Your TMDB API key
TMDB_API_KEY = '39d781d16ae58372fa607e5d412b1bc3'


def movie_search(request):
    form = MovieSearchForm()
    movies = None

    if request.method == 'POST':
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={query}'

            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                movies = data['results']  # Get list of movies

    return render(request, 'search.html', {'form': form, 'movies': movies})


def movie_detail(request, movie_id):
    # API URL to get movie details by ID
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}'

    response = requests.get(url)
    movie = None

    if response.status_code == 200:
        movie = response.json()  # Get movie details from response

    return render(request, 'detail.html', {'movie': movie})

