from rest_framework.viewsets import ModelViewSet

from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer
