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

def save_movie(request, movie_id):
    # Check if the movie is already saved
    if SavedMovie.objects.filter(movie_id=movie_id).exists():
        return redirect('movie_detail', movie_id=movie_id)

    # Fetch movie details from TMDB API
    movie_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}'
    response = requests.get(movie_url)
    if response.status_code == 200:
        movie_data = response.json()
        # Save the movie to the database
        saved_movie = SavedMovie(
            movie_id=movie_data['id'],
            title=movie_data['title'],
            overview=movie_data['overview'],
            poster_path=movie_data['poster_path']
        )
        saved_movie.save()

    return redirect('movie_detail', movie_id=movie_id)

def bookmarked_movies(request):
    saved_movies = save_movie.objects.all()
    return render(request, 'moviedetails/bookmarked.html', {'saved_movies': saved_movies})

