# 🧠 Building Quiz AI API with Django REST Framework 📝

> A simple guide to create a Quiz AI API using Django REST Framework - Split into two parts for easy learning!

## 📋 Table of Contents
- [🎯 What We're Building](#what-were-building)
- [⚙️ Setup](#setup)
- [📦 Part 1: Basic Quiz CRUD](#part-1-basic-quiz-crud)
- [🧪 Testing Part 1](#testing-part-1)
- [🚀 Part 2: Questions & Choices](#part-2-questions--choices)
- [🧪 Testing Part 2](#testing-part-2)
- [🔮 Next Steps](#next-steps)

## 🎯 What We're Building

**Part 1:** Simple Quiz CRUD operations
**Part 2:** Complete quiz system with questions and choices

### 🌐 Final API Endpoints
- `GET /api/v1/quizzes/` - 📋 List all quizzes
- `POST /api/v1/quizzes/` - ➕ Create new quiz
- `GET /api/v1/quizzes/<id>/` - 🎯 Get specific quiz
- `PUT /api/v1/quizzes/<id>/` - ✏️ Update quiz
- `DELETE /api/v1/quizzes/<id>/` - 🗑️ Delete quiz
- `POST /api/v1/quizzes/<id>/validate/` - ✅ Validate answers (Part 2)

## ⚙️ Setup

### 📁 Create Project
```bash
mkdir quiz_ai
cd quiz_ai
```

### 🐍 Virtual Environment
```bash
# Mac/Linux
python3 -m venv venv
source venv/bin/activate

# Windows  
python -m venv venv
venv\Scripts\activate
```

> 📝 **Git Note:** Add `venv/` to your `.gitignore` file to avoid committing virtual environment files

> 💡 **Windows Note:** Use `python` instead of `python3` on Windows systems

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
**Edit `config/settings.py`:**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # 🆕 Django REST Framework
    'quizzes',         # 🆕 Our quiz app
]

# 🆕 Django REST Framework Configuration
REST_FRAMEWORK = {
    # 🔓 Allow anyone to access API (for development only!)
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    # 📄 Add pagination to API responses
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10  # 📊 Show 10 items per page
}
```

> 🗃️ **SQLite Note:** You can add `db.sqlite3` to `.gitignore`. To regenerate: just run `python manage.py migrate` and it will create a new database.

---

## 📦 Part 1: Basic Quiz CRUD

Let's start with a simple Quiz model and complete CRUD operations!

### 🗄️ Step 1: Create Quiz Model
**Edit `quizzes/models.py`:**
```python
from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "quizzes"  # 📝 Proper plural form
        ordering = ['-created_at']       # 📅 Newest first
    
    def __str__(self):
        return self.title
```

### 🔄 Step 2: Create Serializer
**Create `quizzes/serializers.py`:**
```python
from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    """🔄 Converts Quiz model to/from JSON"""
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']  # 🔒 Auto-generated fields
```

### 👀 Step 3: Create Views (The Magic!)
**Edit `quizzes/views.py`:**
```python
from rest_framework import viewsets
from .models import Quiz
from .serializers import QuizSerializer

class QuizViewSet(viewsets.ModelViewSet):
    """
    🪄 ModelViewSet automatically provides:
    - GET /api/v1/quizzes/ (list)
    - POST /api/v1/quizzes/ (create) 
    - GET /api/v1/quizzes/<id>/ (retrieve)
    - PUT /api/v1/quizzes/<id>/ (update)
    - PATCH /api/v1/quizzes/<id>/ (partial update)
    - DELETE /api/v1/quizzes/<id>/ (destroy)
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
```

> 🎯 **Super Class:** `ModelViewSet` is the "super class" that wraps all CRUD operations. It's DRF's magic! ✨

### 🛣️ Step 4: Setup URLs with v1
**Create `quizzes/urls.py`:**
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet

# 🤖 Router automatically creates RESTful URLs
router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),  # 🆕 Version 1 prefix
]
```

**Edit `config/urls.py`:**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('quizzes.urls')),        # 🆕 API routes
    path('api-auth/', include('rest_framework.urls')),  # 🆕 DRF auth UI
]
```

### 🗄️ Step 5: Admin Panel (Optional but Helpful!)
**Edit `quizzes/admin.py`:**
```python
from django.contrib import admin
from .models import Quiz

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']     # 📋 Show these columns
    search_fields = ['title', 'description']   # 🔍 Enable search
    list_filter = ['created_at']               # 🗂️ Filter sidebar
```

### 📊 Step 6: Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # 👤 For admin access
```

## 🧪 Testing Part 1

### 🚀 Run Server
```bash
python manage.py runserver
```

### 🌐 Test Your API

**1. 📋 List All Quizzes**
```
GET http://127.0.0.1:8000/api/v1/quizzes/
```

**2. ➕ Create New Quiz**
```bash
curl -X POST http://127.0.0.1:8000/api/v1/quizzes/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Python Basics 🐍",
    "description": "Test your Python knowledge!"
  }'
```

**3. 🎯 Get Specific Quiz**
```
GET http://127.0.0.1:8000/api/v1/quizzes/1/
```

**4. ✏️ Update Quiz**
```bash
curl -X PUT http://127.0.0.1:8000/api/v1/quizzes/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Advanced Python 🚀",
    "description": "Master Python concepts!"
  }'
```

**5. 🗑️ Delete Quiz**
```bash
curl -X DELETE http://127.0.0.1:8000/api/v1/quizzes/1/
```

### 📱 Browser Testing
- Visit `http://127.0.0.1:8000/api/v1/quizzes/` for the beautiful DRF interface! 🎨
- Admin panel: `http://127.0.0.1:8000/admin/` 🛠️

---

## 🚀 Part 2: Questions & Choices

Now let's add the quiz logic with questions and choices!

### 🗄️ Step 1: Extend Models
**Edit `quizzes/models.py` - ADD these models:**
```python
# Keep existing Quiz model and ADD these:

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text[:50] + "..." if len(self.text) > 50 else self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{'✅' if self.is_correct else '❌'} {self.text}"
```

### 🔄 Step 2: Update Serializers
**Edit `quizzes/serializers.py` - ADD these serializers:**
```python
# Keep existing QuizSerializer and ADD these:

class ChoiceSerializer(serializers.ModelSerializer):
    """📝 Serializer for answer choices"""
    class Meta:
        model = Choice
        fields = ['id', 'text', 'is_correct']

class QuestionDetailSerializer(serializers.ModelSerializer):
    """❓ Question with all its choices"""
    choices = ChoiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'choices']

class QuizDetailSerializer(serializers.ModelSerializer):
    """🎯 Complete quiz with questions and choices"""
    questions = QuestionDetailSerializer(many=True, read_only=True)
    questions_count = serializers.SerializerMethodField()  # 📊 Extra info
    
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'questions', 'questions_count']
    
    def get_questions_count(self, obj):
        return obj.questions.count()

class AnswerSerializer(serializers.Serializer):
    """✅ For validating submitted answers"""
    question_id = serializers.IntegerField()
    choice_id = serializers.IntegerField()
```

### 👀 Step 3: Update Views
**Edit `quizzes/views.py` - UPDATE the QuizViewSet:**
```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Quiz, Question, Choice
from .serializers import QuizSerializer, QuizDetailSerializer, AnswerSerializer

class QuizViewSet(viewsets.ModelViewSet):
    """🎯 Complete Quiz API with validation"""
    queryset = Quiz.objects.all()
    
    def get_serializer_class(self):
        """🔄 Use detailed serializer for single quiz view"""
        if self.action == 'retrieve':
            return QuizDetailSerializer
        return QuizSerializer
    
    @action(detail=True, methods=['post'])
    def validate(self, request, pk=None):
        """✅ Validate submitted quiz answers"""
        quiz = self.get_object()
        
        # 📝 Validate incoming data
        serializer = AnswerSerializer(data=request.data.get('answers', []), many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # 🧮 Process answers
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
                    'choice_id': choice_id,
                    'correct': choice.is_correct,
                    'question_text': question.text,
                    'choice_text': choice.text
                })
            except (Question.DoesNotExist, Choice.DoesNotExist):
                results.append({
                    'question_id': question_id,
                    'error': 'Question or choice not found ❌'
                })
        
        # 📊 Calculate score
        correct_answers = sum(1 for r in results if r.get('correct', False))
        total_answers = len(results)
        percentage = int((correct_answers / total_answers) * 100) if total_answers else 0
        
        return Response({
            'quiz_id': quiz.id,
            'quiz_title': quiz.title,
            'score': f"{correct_answers}/{total_answers}",
            'percentage': percentage,
            'grade': '🏆' if percentage >= 80 else '👍' if percentage >= 60 else '📚',
            'results': results
        })
```

### 🗄️ Step 4: Update Admin
**Edit `quizzes/admin.py` - ADD new admin classes:**
```python
from django.contrib import admin
from .models import Quiz, Question, Choice

# Keep existing QuizAdmin and ADD these:

class ChoiceInline(admin.TabularInline):
    """📝 Edit choices directly in question form"""
    model = Choice
    extra = 4  # Show 4 empty choice fields

class QuestionInline(admin.TabularInline):
    """❓ Edit questions directly in quiz form"""
    model = Question
    extra = 2  # Show 2 empty question fields

# UPDATE existing QuizAdmin:
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'questions_count']
    search_fields = ['title', 'description']
    list_filter = ['created_at']
    inlines = [QuestionInline]  # 🆕 Edit questions inline
    
    def questions_count(self, obj):
        return obj.questions.count()
    questions_count.short_description = 'Questions'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text_preview', 'quiz', 'choices_count']
    list_filter = ['quiz']
    search_fields = ['text']
    inlines = [ChoiceInline]  # 🆕 Edit choices inline
    
    def text_preview(self, obj):
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Question'
    
    def choices_count(self, obj):
        return obj.choices.count()
    choices_count.short_description = 'Choices'

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['text', 'question_preview', 'is_correct']
    list_filter = ['is_correct', 'question__quiz']
    search_fields = ['text']
    
    def question_preview(self, obj):
        return obj.question.text[:30] + "..." if len(obj.question.text) > 30 else obj.question.text
    question_preview.short_description = 'Question'
```

### 📊 Step 5: Create New Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🧪 Testing Part 2

### 🎯 Complete Quiz Example

**1. 📋 Get Quiz with Questions (GET)**
```
GET http://127.0.0.1:8000/api/v1/quizzes/1/
```

**Response:**
```json
{
  "id": 1,
  "title": "Python Basics 🐍",
  "description": "Test your Python knowledge!",
  "created_at": "2024-01-01T10:00:00Z",
  "questions_count": 2,
  "questions": [
    {
      "id": 1,
      "text": "What is Python?",
      "choices": [
        {"id": 1, "text": "A programming language", "is_correct": true},
        {"id": 2, "text": "A snake", "is_correct": false}
      ]
    }
  ]
}
```

**2. ✅ Validate Quiz Answers (POST)**
```bash
curl -X POST http://127.0.0.1:8000/api/v1/quizzes/1/validate/ \
  -H "Content-Type: application/json" \
  -d '{
    "answers": [
      {"question_id": 1, "choice_id": 1},
      {"question_id": 2, "choice_id": 3}
    ]
  }'
```

**Response:**
```json
{
  "quiz_id": 1,
  "quiz_title": "Python Basics 🐍",
  "score": "2/2",
  "percentage": 100,
  "grade": "🏆",
  "results": [
    {
      "question_id": 1,
      "choice_id": 1,
      "correct": true,
      "question_text": "What is Python?",
      "choice_text": "A programming language"
    }
  ]
}
```

## 🔮 Next Steps

### 🚀 Immediate Enhancements
- ⏱️ **Timed Quizzes** - Add time limits
- 🏷️ **Categories** - Organize by topics  
- 🔐 **Authentication** - User accounts
- 📊 **Leaderboards** - Track high scores
- 🖼️ **Media Questions** - Images/videos

### 📚 Learning Challenges
- Add user registration and login
- Implement quiz sharing via unique links
- Add difficulty levels and point systems
- Create quiz analytics dashboard
- Build a React frontend

### 🎯 What You've Learned
- ✅ Django REST Framework basics
- ✅ ModelViewSet magic for CRUD operations  
- ✅ Model relationships (ForeignKey)
- ✅ Custom API endpoints with @action
- ✅ Nested serializers
- ✅ API versioning (v1)
- ✅ Admin panel customization

---

🎉 **Congratulations!** You've built a complete Quiz AI API with Django REST Framework! 🎊

Your API now supports full CRUD operations for quizzes and includes a smart validation system for quiz answers. The ModelViewSet gave you all CRUD endpoints automatically - that's the power of Django REST Framework! ⚡️