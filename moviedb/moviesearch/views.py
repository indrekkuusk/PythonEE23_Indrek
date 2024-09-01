# import requests
# from django.shortcuts import render
# from django.conf import settings
# from .forms import MovieSearchForm
#
#
# def movie_search(request):
#     movies = []
#     error_message = None
#
#     if request.method == 'POST':
#         form = MovieSearchForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             api_key = settings.TMDB_API_KEY  # Store your API key in settings.py
#             url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}"
#
#             try:
#                 response = requests.get(url)
#                 response.raise_for_status()  # Raise an HTTPError for bad responses
#
#                 data = response.json()
#                 movies = data.get('results', [])
#
#             except requests.exceptions.RequestException as e:
#                 error_message = f"An error occurred: {e}"
#
#     else:
#         form = MovieSearchForm()
#
#     return render(request, 'moviesearch/movie_search.html',
#                   {'form': form, 'movies': movies, 'error_message': error_message})
# moviesearch/views.py
import requests
from django.shortcuts import render
from django.conf import settings
from .forms import MovieSearchForm


def movie_search(request):
    movies = []
    error_message = None

    if request.method == 'POST':
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            api_key = settings.TMDB_API_KEY
            url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}"

            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                movies = data.get('results', [])

            except requests.exceptions.RequestException as e:
                error_message = f"An error occurred: {e}"

    else:
        form = MovieSearchForm()

    return render(request, 'moviesearch/movie_search.html',
                  {'form': form, 'movies': movies, 'error_message': error_message})


def movie_detail(request, movie_id):
    api_key = settings.TMDB_API_KEY
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    movie = None
    error_message = None

    try:
        response = requests.get(url)
        response.raise_for_status()
        movie = response.json()

    except requests.exceptions.RequestException as e:
        error_message = f"An error occurred: {e}"

    return render(request, 'moviesearch/movie_detail.html', {'movie': movie, 'error_message': error_message})
