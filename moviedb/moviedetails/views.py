import requests
from django.shortcuts import render
from django.conf import settings

def movie_detail_view(request, movie_id):
    """
    Retrieve detailed movie information from TMDB API using the movie ID.
    """
    api_key = settings.TMDB_API_KEY
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&append_to_response=credits"
    movie = None
    error_message = None

    try:
        response = requests.get(url)
        response.raise_for_status()
        movie = response.json()

    except requests.exceptions.RequestException as e:
        error_message = f"An error occurred: {e}"

    return render(request, 'moviedetails/movie_detail.html', {'movie': movie, 'error_message': error_message})
