from rest_framework.routers import DefaultRouter

from .views import MovieViewSet, GenreViewSet

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("genres", GenreViewSet, basename="genre")

urlpatterns = router.urls
