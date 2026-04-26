from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    synopsis = models.TextField()
    release_date = models.DateField()
    duration_minutes = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    genres = models.ManyToManyField(Genre, related_name="movies")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-release_date", "title"]

    def __str__(self):
        return self.title
