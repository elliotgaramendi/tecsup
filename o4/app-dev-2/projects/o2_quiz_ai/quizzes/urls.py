from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)

urlpatterns = [
    path('', include(router.urls)),
]