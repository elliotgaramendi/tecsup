# 🧠 Building a Quiz API with Django REST Framework 📝

> A simple guide to create a Quiz API using Django REST Framework

## 📋 Table of Contents
- [What We're Building](#what-were-building)
- [Setup](#setup)
- [Implementation](#implementation)
- [Testing](#testing)
- [Next Steps](#next-steps)

## What We're Building

We'll create a Quiz API that allows users to:
- ✅ Create, read, update, and delete quizzes
- ❓ Add questions with multiple choices
- 📊 Submit answers and get validation results

### 🏗️ Main Components
```
Quiz API
├── 📚 Models (Quiz, Question, Choice)
├── 🔄 Serializers (Data conversion)
├── 👀 Views (API logic)
└── 🛣️ URLs (Routing)
```

### 🌐 API Endpoints
- `/api/quizzes/` - 📋 List all quizzes
- `/api/quizzes/<id>/` - 🎯 Specific quiz details
- `/api/questions/` - ❓ All questions
- `/api/choices/` - 📝 All choices
- `/api/quizzes/<id>/validate/` - ✅ Validate answers

## Setup

### 📁 Create Project
```bash
mkdir quiz_api
cd quiz_api
```

### 🐍 Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows
```

### 📦 Install Dependencies
```bash
pip install django djangorestframework
pip freeze > requirements.txt
```

### 🎛️ Django Setup
```bash
django-admin startproject config .
python manage.py startapp quizzes
```

### ⚙️ Settings Configuration
Add to `config/settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # 🆕
    'quizzes',         # 🆕
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

## Implementation

### 🗄️ Models (`quizzes/models.py`)
```python
from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    
    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
```

### 🔄 Serializers (`quizzes/serializers.py`)
```python
from rest_framework import serializers
from .models import Quiz, Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct']

class QuestionDetailSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text', 'choices']

class QuizDetailSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'questions']
    
    def get_questions(self, obj):
        questions = obj.questions.all()
        return QuestionDetailSerializer(questions, many=True).data

class AnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()
```

### 👀 Views (`quizzes/views.py`)
```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Quiz, Question, Choice
from .serializers import QuizDetailSerializer, AnswerSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer
    
    @action(detail=True, methods=['post'])
    def validate(self, request, pk=None):
        """✅ Validate quiz answers"""
        quiz = self.get_object()
        
        serializer = AnswerSerializer(data=request.data.get('answers', []), many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        answers = serializer.validated_data
        results = []
        
        for answer in answers:
            question_id = answer['question_id']
            choice_id = answer['choice_id']
            
            try:
                question = Question.objects.get(id=question_id, quiz=quiz)
                choice = Choice.objects.get(id=choice_id, question=question)
                
                results.append({
                    'question_id': question_id,
                    'correct': choice.is_correct
                })
            except (Question.DoesNotExist, Choice.DoesNotExist):
                results.append({
                    'question_id': question_id,
                    'error': 'Question or choice not found'
                })
        
        correct_answers = sum(1 for r in results if r.get('correct', False))
        total_answers = len(results)
        
        return Response({
            'quiz_id': quiz.id,
            'score': f"{correct_answers}/{total_answers}",
            'percentage': int((correct_answers / total_answers) * 100) if total_answers else 0,
            'results': results
        })
```

### 🛣️ URLs (`quizzes/urls.py`)
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

### 🔗 Main URLs (`config/urls.py`)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('quizzes.urls')),
]
```

### 🗃️ Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Testing

### 🚀 Run Server
```bash
python manage.py runserver
```

### 🌐 Browser Testing
Visit these URLs:
- 📋 `http://127.0.0.1:8000/api/quizzes/` - All quizzes
- 🎯 `http://127.0.0.1:8000/api/quizzes/1/` - Specific quiz
- 🔧 `http://127.0.0.1:8000/admin/` - Admin panel

### 📡 API Testing Examples

**Create Quiz:**
```bash
curl -X POST http://127.0.0.1:8000/api/quizzes/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Python Basics 🐍", "description": "Test your Python knowledge"}'
```

**Validate Answers:**
```bash
curl -X POST http://127.0.0.1:8000/api/quizzes/1/validate/ \
  -H "Content-Type: application/json" \
  -d '{"answers": [{"question_id": 1, "choice_id": 1}]}'
```

**Expected Response:**
```json
{
  "quiz_id": 1,
  "score": "1/1",
  "percentage": 100,
  "results": [
    {
      "question_id": 1,
      "correct": true
    }
  ]
}
```

## Next Steps

### 🔮 Additional Features
- ⏱️ **Timed Quizzes** - Add time limits
- 👥 **User System** - Authentication & profiles
- 🏷️ **Categories** - Organize quizzes by topic
- 📊 **Analytics** - Track quiz performance
- 🖼️ **Media Support** - Images in questions
- 💬 **Feedback** - Explanations for answers

### 📱 Potential Apps
1. **👤 User Management** - Handle user profiles and attempts
2. **🏷️ Categories & Tags** - Organize quizzes better
3. **📈 Analytics Dashboard** - Track quiz statistics

### 🎯 Learning Goals Achieved
- ✅ Django REST Framework basics
- ✅ Model relationships (ForeignKey)
- ✅ Nested serializers
- ✅ Custom API endpoints
- ✅ Data validation
- ✅ API testing

---

🎉 **Congratulations!** You've built a complete Quiz API with Django REST Framework! 🎊