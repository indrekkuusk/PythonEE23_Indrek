from django.db import models

# Create your models here.
from django.db import models

class SavedMovie(models.Model):
    movie_id = models.IntegerField()  # TMDB movie ID
    title = models.CharField(max_length=255)
    overview = models.TextField()
    poster_path = models.CharField(max_length=255)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
