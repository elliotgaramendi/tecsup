from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    release_year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
