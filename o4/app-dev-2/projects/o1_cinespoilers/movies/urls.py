from django.urls import path

from .views import movie_list

app_name = "movies"

urlpatterns = [
    path("", movie_list, name="list"),
]
