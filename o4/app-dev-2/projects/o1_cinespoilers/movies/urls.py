from django.urls import path
from .views import movie_list

urlpatterns = [
    path('', movie_list, name='movie_list'),
]
