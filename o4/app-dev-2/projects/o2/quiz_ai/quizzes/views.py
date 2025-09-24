from rest_framework import viewsets
from .models import Quiz
from .serializers import QuizSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
