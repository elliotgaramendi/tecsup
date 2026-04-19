from rest_framework.routers import DefaultRouter

from .views import MovieViewSet

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = router.urls
