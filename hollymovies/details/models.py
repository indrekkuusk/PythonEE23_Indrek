from django.db import models

# Create your models here.
from django.db.models import CharField, Model


class Genre(Model):
    name = CharField(max_length=128)
