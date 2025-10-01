from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Quiz, Question, Choice
from .serializers import QuizSerializer, QuestionSerializer, ChoiceSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'message': 'Quiz API v1',
        'endpoints': {
            'quizzes': reverse('quiz-list', request=request, format=format),
            'questions': reverse('question-list', request=request, format=format),
            'choices': reverse('choice-list', request=request, format=format),
        }
    })


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
