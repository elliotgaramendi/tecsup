# 🧠 Building a Quiz API with Django REST Framework

> A clean, gradual guide to building a complete Quiz API - Learn by doing!

## 📋 Table of Contents
- [What We're Building](#what-were-building)
- [Initial Setup](#initial-setup)
- [Part 1: Quiz CRUD](#part-1-quiz-crud)
- [Part 2: Questions & Choices](#part-2-questions--choices)
- [Part 3: Answer Validation](#part-3-answer-validation)
- [Next Steps](#next-steps)

---

## 🎯 What We're Building

A RESTful Quiz API that allows you to:
- Create and manage quizzes
- Add questions with multiple choices
- Submit answers and get instant grading

**Learning Path:**
1. **Part 1** - Basic Quiz CRUD operations
2. **Part 2** - Add Questions and Choices with relationships
3. **Part 3** - Implement answer validation and scoring

---

## ⚙️ Initial Setup

### Create Project Structure
```bash
mkdir quiz_api && cd quiz_api
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install django djangorestframework
django-admin startproject config .
python manage.py startapp quizzes
```

### Configure Settings
**Edit `config/settings.py`:**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'quizzes',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

---

## 📦 Part 1: Quiz CRUD

### Model
**`quizzes/models.py`:**
```python
from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "quizzes"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
```

### Serializer
**`quizzes/serializers.py`:**
```python
from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
```

### Views
**`quizzes/views.py`:**
```python
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Quiz
from .serializers import QuizSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'message': 'Quiz API v1',
        'endpoints': {
            'quizzes': reverse('quiz-list', request=request, format=format),
        }
    })

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
```

### URLs
**`quizzes/urls.py`:**
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, api_root

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]
```

**`config/urls.py`:**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('quizzes.urls')),
]
```

### Migrate and Run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Test Part 1
```bash
# View API root
curl http://127.0.0.1:8000/api/v1/

# Create quiz
curl -X POST http://127.0.0.1:8000/api/v1/quizzes/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Python Basics", "description": "Test your Python knowledge"}'

# List quizzes
curl http://127.0.0.1:8000/api/v1/quizzes/

# Get quiz detail
curl http://127.0.0.1:8000/api/v1/quizzes/1/

# Update quiz
curl -X PUT http://127.0.0.1:8000/api/v1/quizzes/1/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Advanced Python", "description": "Master Python"}'

# Delete quiz
curl -X DELETE http://127.0.0.1:8000/api/v1/quizzes/1/
```

**✅ Part 1 Complete!** You have a working Quiz CRUD API.

---

## 🔗 Part 2: Questions & Choices

### Models
**Add to `quizzes/models.py`:**
```python
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text[:50]

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
```

### Serializers
**Add to `quizzes/serializers.py`:**
```python
from .models import Quiz, Question, Choice

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text', 'created_at']
        read_only_fields = ['created_at']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'text', 'is_correct']
```

### Views
**Add to `quizzes/views.py`:**
```python
from .models import Quiz, Question, Choice
from .serializers import QuizSerializer, QuestionSerializer, ChoiceSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
```

**Update `api_root` in `quizzes/views.py`:**
```python
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
```

### URLs
**Update `quizzes/urls.py`:**
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet, api_root

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]
```

### Migrate
```bash
python manage.py makemigrations
python manage.py migrate
```

### Test Part 2
```bash
# Create quiz
curl -X POST http://127.0.0.1:8000/api/v1/quizzes/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Python Quiz", "description": "Basic Python"}'

# Create question
curl -X POST http://127.0.0.1:8000/api/v1/questions/ \
  -H "Content-Type: application/json" \
  -d '{"quiz": 2, "text": "What is Python?"}'

# Create correct choice
curl -X POST http://127.0.0.1:8000/api/v1/choices/ \
  -H "Content-Type: application/json" \
  -d '{"question": 1, "text": "A programming language", "is_correct": true}'

# Create incorrect choice
curl -X POST http://127.0.0.1:8000/api/v1/choices/ \
  -H "Content-Type: application/json" \
  -d '{"question": 1, "text": "A snake", "is_correct": false}'

# List all questions
curl http://127.0.0.1:8000/api/v1/questions/

# List all choices
curl http://127.0.0.1:8000/api/v1/choices/
```

**✅ Part 2 Complete!** You can now create complete quizzes with questions and choices.

---

## ✅ Part 3: Answer Validation

### Enhanced Serializers
**Add to `quizzes/serializers.py`:**
```python
class ChoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text']

class QuestionDetailSerializer(serializers.ModelSerializer):
    choices = ChoiceDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'choices']

class QuizDetailSerializer(serializers.ModelSerializer):
    questions = QuestionDetailSerializer(many=True, read_only=True)
    question_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'question_count', 'questions']
    
    def get_question_count(self, obj):
        return obj.questions.count()

class SubmitAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()
```

### Enhanced QuizViewSet
**Update `QuizViewSet` in `quizzes/views.py`:**
```python
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Quiz, Question, Choice
from .serializers import (
    QuizSerializer, QuestionSerializer, ChoiceSerializer,
    QuizDetailSerializer, SubmitAnswerSerializer
)

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuizDetailSerializer
        return QuizSerializer
    
    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        quiz = self.get_object()
        serializer = SubmitAnswerSerializer(data=request.data.get('answers', []), many=True)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        answers = serializer.validated_data
        results = []
        correct_count = 0
        
        for answer in answers:
            try:
                question = Question.objects.get(id=answer['question_id'], quiz=quiz)
                choice = Choice.objects.get(id=answer['choice_id'], question=question)
                
                is_correct = choice.is_correct
                if is_correct:
                    correct_count += 1
                
                results.append({
                    'question_id': question.id,
                    'question_text': question.text,
                    'choice_id': choice.id,
                    'choice_text': choice.text,
                    'is_correct': is_correct
                })
            except (Question.DoesNotExist, Choice.DoesNotExist):
                results.append({
                    'question_id': answer['question_id'],
                    'error': 'Invalid question or choice'
                })
        
        total = len(results)
        percentage = round((correct_count / total) * 100, 2) if total > 0 else 0
        
        grade_map = {
            90: ('A', '🏆'),
            80: ('B', '🎉'),
            70: ('C', '👍'),
            60: ('D', '📚'),
            0: ('F', '💪')
        }
        
        grade, emoji = next((g, e) for threshold, (g, e) in sorted(grade_map.items(), reverse=True) if percentage >= threshold)
        
        return Response({
            'quiz_id': quiz.id,
            'quiz_title': quiz.title,
            'total_questions': total,
            'correct_answers': correct_count,
            'score': f"{correct_count}/{total}",
            'percentage': percentage,
            'grade': grade,
            'emoji': emoji,
            'results': results
        })
```

### Test Part 3
```bash
# Get complete quiz with questions
curl http://127.0.0.1:8000/api/v1/quizzes/1/

# Submit answers
curl -X POST http://127.0.0.1:8000/api/v1/quizzes/1/submit/ \
  -H "Content-Type: application/json" \
  -d '{
    "answers": [
      {"question_id": 1, "choice_id": 1},
      {"question_id": 2, "choice_id": 3}
    ]
  }'
```

**Expected Response:**
```json
{
  "quiz_id": 1,
  "quiz_title": "Python Quiz",
  "total_questions": 2,
  "correct_answers": 2,
  "score": "2/2",
  "percentage": 100.0,
  "grade": "A",
  "emoji": "🏆",
  "results": [
    {
      "question_id": 1,
      "question_text": "What is Python?",
      "choice_id": 1,
      "choice_text": "A programming language",
      "is_correct": true
    }
  ]
}
```

**✅ Part 3 Complete!** Your Quiz API is fully functional!

---

## 🎯 Complete Workflow Example

```bash
# 1. Create quiz
curl -X POST http://127.0.0.1:8000/api/v1/quizzes/ \
  -H "Content-Type: application/json" \
  -d '{"title": "JavaScript Basics", "description": "JS fundamentals"}'

# 2. Add questions
curl -X POST http://127.0.0.1:8000/api/v1/questions/ \
  -H "Content-Type: application/json" \
  -d '{"quiz": 1, "text": "What is a variable?"}'

curl -X POST http://127.0.0.1:8000/api/v1/questions/ \
  -H "Content-Type: application/json" \
  -d '{"quiz": 1, "text": "What is a function?"}'

# 3. Add choices for question 1
curl -X POST http://127.0.0.1:8000/api/v1/choices/ \
  -H "Content-Type: application/json" \
  -d '{"question": 1, "text": "A container for data", "is_correct": true}'

curl -X POST http://127.0.0.1:8000/api/v1/choices/ \
  -H "Content-Type: application/json" \
  -d '{"question": 1, "text": "A loop", "is_correct": false}'

# 4. Add choices for question 2
curl -X POST http://127.0.0.1:8000/api/v1/choices/ \
  -H "Content-Type: application/json" \
  -d '{"question": 2, "text": "A reusable block of code", "is_correct": true}'

curl -X POST http://127.0.0.1:8000/api/v1/choices/ \
  -H "Content-Type: application/json" \
  -d '{"question": 2, "text": "A variable", "is_correct": false}'

# 5. View complete quiz
curl http://127.0.0.1:8000/api/v1/quizzes/1/

# 6. Submit answers
curl -X POST http://127.0.0.1:8000/api/v1/quizzes/1/submit/ \
  -H "Content-Type: application/json" \
  -d '{"answers": [{"question_id": 1, "choice_id": 1}, {"question_id": 2, "choice_id": 3}]}'
```

---

## 📚 What You've Learned

**Part 1 - Foundations**
- Django REST Framework setup
- ModelViewSet for automatic CRUD
- Basic serializers and routing

**Part 2 - Relationships**
- ForeignKey relationships
- Multiple ViewSets
- Related models (Quiz → Question → Choice)

**Part 3 - Advanced**
- Custom actions with `@action`
- Nested serializers
- Dynamic serializer selection
- Business logic implementation

---

## 🚀 Next Steps

### Enhancement Ideas
- **Authentication**: Add user accounts with JWT
- **Categories**: Organize quizzes by topic
- **Time Limits**: Add countdown timers
- **Leaderboards**: Track top scores
- **Images**: Add media to questions
- **Analytics**: Track user performance
- **Random Order**: Shuffle questions/choices

### Production Ready
```python
# Add to settings.py for production
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

### Testing
```python
# tests.py
from rest_framework.test import APITestCase

class QuizAPITest(APITestCase):
    def test_create_quiz(self):
        response = self.client.post('/api/v1/quizzes/', {
            'title': 'Test Quiz',
            'description': 'Test'
        })
        self.assertEqual(response.status_code, 201)
```

---

## 📖 API Reference

| Method | Endpoint                       | Description       |
| ------ | ------------------------------ | ----------------- |
| GET    | `/api/v1/`                     | API documentation |
| GET    | `/api/v1/quizzes/`             | List quizzes      |
| POST   | `/api/v1/quizzes/`             | Create quiz       |
| GET    | `/api/v1/quizzes/{id}/`        | Get quiz details  |
| PUT    | `/api/v1/quizzes/{id}/`        | Update quiz       |
| DELETE | `/api/v1/quizzes/{id}/`        | Delete quiz       |
| POST   | `/api/v1/quizzes/{id}/submit/` | Submit answers    |
| GET    | `/api/v1/questions/`           | List questions    |
| POST   | `/api/v1/questions/`           | Create question   |
| GET    | `/api/v1/choices/`             | List choices      |
| POST   | `/api/v1/choices/`             | Create choice     |

---

## 🎉 Congratulations!

You've built a complete Quiz API with:
- ✅ Full CRUD operations
- ✅ Model relationships
- ✅ Answer validation
- ✅ Scoring system
- ✅ Clean, maintainable code

**Ready for production? Add authentication, tests, and deploy!** 🚀