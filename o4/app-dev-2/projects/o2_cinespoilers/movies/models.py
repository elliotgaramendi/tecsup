from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True)
    release_date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "movies"
        ordering = ["-created_at"]
        verbose_name = "movie"
        verbose_name_plural = "movies"

    def __str__(self) -> str:
        return self.title
