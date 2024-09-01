from django.db import models
from django.contrib.auth.models import User

class SavedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_movies')
    movie_id = models.IntegerField()
    title = models.CharField(max_length=255)
    release_date = models.CharField(max_length=10, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    poster_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

