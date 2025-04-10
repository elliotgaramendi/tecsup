# Guide: Simple Quiz Application with Django 🧠📝

This guide will show you how to create a basic quiz application with Django, with features to create exams, add questions, and specify correct answers.

## 📋 Application Structure

We'll create 3 main routes:
- List of exams
- Details of an exam with its questions
- Form to create exams and questions

## Step 1: Environment Setup 🛠️

```bash
# Create project directory
mkdir quiz_app
cd quiz_app

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Create src directory (similar structure to frontend projects)
mkdir src
cd src

# Install Django
pip3 install django

# Create a requirements.txt file
pip3 freeze > requirements.txt
```

**Note**: If you're using Git, create a `.gitignore` file at the project root:

```bash
# Return to the project root
cd ..

# Create .gitignore file
echo "__pycache__/
*.py[cod]
*$py.class
*.so
.Python
db.sqlite3
.env
venv/
.vscode/" > .gitignore
```

This will prevent versioning unnecessary files like Python cache, SQLite database, and the virtual environment.

## Step 2: Create the Django Project 🚀

```bash
# Make sure you're in the src directory
cd src

# Create project
django-admin startproject config .

# Create application
python3 manage.py startapp quiz
```

## Step 3: Basic Configuration ⚙️

Edit `config/settings.py` to include the app:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quiz',  # Our application
]
```

## Step 4: Define the Models 🏗️

Edit `quiz/models.py`:

```python
from django.db import models

class Exam(models.Model):
    """Model for exams"""
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_question_count(self):
        """Returns the number of questions in this exam"""
        return self.questions.count()

class Question(models.Model):
    """Model for questions"""
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name="Question text")
    
    def __str__(self):
        return self.text[:50]

class Choice(models.Model):
    """Model for answer choices"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200, verbose_name="Text")
    is_correct = models.BooleanField(default=False, verbose_name="Is correct")
    
    def __str__(self):
        return self.text
```

## Step 5: Migrate the Database 💾

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

**Note**: Remember that migration files (in `migrations/`) should be versioned, but the `db.sqlite3` file should be excluded from version control (it's already in the `.gitignore` we created).

## Step 6: Create Forms 📝

Create file `quiz/forms.py`:

```python
from django import forms
from .models import Exam, Question, Choice

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text', 'is_correct']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# Create formset for options
ChoiceFormSet = forms.inlineformset_factory(
    Question, Choice, form=ChoiceForm, extra=4, can_delete=False
)
```

## Step 7: Create Views 👁️

Edit `quiz/views.py`:

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from .models import Exam, Question, Choice
from .forms import ExamForm, QuestionForm, ChoiceFormSet

def exam_list(request):
    """View to display a list of all exams"""
    exams = Exam.objects.all().order_by('-created_date')
    return render(request, 'quiz/exam_list.html', {'exams': exams})

def exam_detail(request, exam_id):
    """View to display the details of an exam with its questions"""
    exam = get_object_or_404(Exam, id=exam_id)
    questions = exam.questions.all().prefetch_related('choices')
    return render(request, 'quiz/exam_detail.html', {'exam': exam, 'questions': questions})

def exam_create(request):
    """View to create a new exam"""
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save()
            messages.success(request, 'Exam created successfully.')
            return redirect('question_create', exam_id=exam.id)
    else:
        form = ExamForm()
    
    return render(request, 'quiz/exam_form.html', {'form': form})

def question_create(request, exam_id):
    """View to add questions to an exam"""
    exam = get_object_or_404(Exam, id=exam_id)
    
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        
        if question_form.is_valid():
            with transaction.atomic():
                # Save the question
                question = question_form.save(commit=False)
                question.exam = exam
                question.save()
                
                # Process the formset for choices
                formset = ChoiceFormSet(request.POST, instance=question)
                if formset.is_valid():
                    formset.save()
                    
                    # Verify that only one option is marked as correct
                    correct_count = question.choices.filter(is_correct=True).count()
                    if correct_count != 1:
                        messages.warning(request, 'There must be exactly one correct answer.')
                    else:
                        messages.success(request, 'Question added successfully.')
                        
                    # Decide where to redirect
                    if 'add_another' in request.POST:
                        return redirect('question_create', exam_id=exam.id)
                    else:
                        return redirect('exam_detail', exam_id=exam.id)
    else:
        question_form = QuestionForm()
        formset = ChoiceFormSet()
    
    return render(request, 'quiz/question_form.html', {
        'exam': exam,
        'question_form': question_form,
        'formset': formset,
    })
```

## Step 8: Configure URLs 🔗

Create `quiz/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('exam/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('exam/create/', views.exam_create, name='exam_create'),
    path('exam/<int:exam_id>/question/add/', views.question_create, name='question_create'),
]
```

Edit `config/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),
]
```

## Step 9: Create Templates 🎨

Create directory structure:

```bash
mkdir -p quiz/templates/quiz
```

### Base Template (quiz/templates/base.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Quiz Application{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light mb-4">
        <div class="container">
            <a class="navbar-brand" href="{% url 'exam_list' %}">Quizzes</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'exam_list' %}">Exams</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'exam_create' %}">Create Exam</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container">
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        {% endif %}

        {% block content %}{% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### Exam List (quiz/templates/quiz/exam_list.html)

```html
{% extends "base.html" %}

{% block title %}Exams{% endblock %}

{% block content %}
<div class="row mb-4">
    <div class="col-md-6">
        <h1>Available Exams</h1>
    </div>
    <div class="col-md-6 text-end">
        <a href="{% url 'exam_create' %}" class="btn btn-primary">Create Exam</a>
    </div>
</div>

<div class="row">
    {% if exams %}
        {% for exam in exams %}
            <div class="col-md-6 mb-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ exam.title }}</h5>
                        <p class="card-text">{{ exam.description|truncatechars:100 }}</p>
                        <p class="text-muted">Questions: {{ exam.get_question_count }}</p>
                        <a href="{% url 'exam_detail' exam.id %}" class="btn btn-primary">View Details</a>
                    </div>
                </div>
            </div>
        {% endfor %}
    {% else %}
        <div class="col-12">
            <div class="alert alert-info">
                No exams available.
                <a href="{% url 'exam_create' %}">Create the first one</a>
            </div>
        </div>
    {% endif %}
</div>
{% endblock %}
```

### Exam Detail (quiz/templates/quiz/exam_detail.html)

```html
{% extends "base.html" %}

{% block title %}{{ exam.title }}{% endblock %}

{% block content %}
<div class="row mb-4">
    <div class="col-md-8">
        <h1>{{ exam.title }}</h1>
        <p>{{ exam.description }}</p>
    </div>
    <div class="col-md-4 text-end">
        <a href="{% url 'question_create' exam.id %}" class="btn btn-primary">Add Question</a>
    </div>
</div>

<div class="mb-4">
    <h2>Questions</h2>
    
    {% if questions %}
        <div class="accordion" id="accordionQuestions">
            {% for question in questions %}
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{{ question.id }}">
                            {{ forloop.counter }}. {{ question.text }}
                        </button>
                    </h2>
                    <div id="collapse{{ question.id }}" class="accordion-collapse collapse" data-bs-parent="#accordionQuestions">
                        <div class="accordion-body">
                            <ul class="list-group">
                                {% for choice in question.choices.all %}
                                    <li class="list-group-item {% if choice.is_correct %}list-group-item-success{% endif %}">
                                        {{ choice.text }} {% if choice.is_correct %}<span class="badge bg-success">Correct</span>{% endif %}
                                    </li>
                                {% empty %}
                                    <li class="list-group-item">No options for this question.</li>
                                {% endfor %}
                            </ul>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    {% else %}
        <div class="alert alert-info">
            This exam doesn't have any questions yet.
            <a href="{% url 'question_create' exam.id %}">Add the first question</a>
        </div>
    {% endif %}
</div>

<div>
    <a href="{% url 'exam_list' %}" class="btn btn-secondary">Back to list</a>
</div>
{% endblock %}
```

### Exam Form (quiz/templates/quiz/exam_form.html)

```html
{% extends "base.html" %}

{% block title %}Create Exam{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-8 offset-md-2">
        <div class="card">
            <div class="card-header">
                <h2>Create New Exam</h2>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="{{ form.title.id_for_label }}" class="form-label">Title</label>
                        {{ form.title }}
                        {% if form.title.errors %}
                            <div class="text-danger">{{ form.title.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.description.id_for_label }}" class="form-label">Description</label>
                        {{ form.description }}
                        {% if form.description.errors %}
                            <div class="text-danger">{{ form.description.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="d-flex justify-content-between">
                        <a href="{% url 'exam_list' %}" class="btn btn-secondary">Cancel</a>
                        <button type="submit" class="btn btn-primary">Continue</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### Question Form (quiz/templates/quiz/question_form.html)

```html
{% extends "base.html" %}

{% block title %}Add Question{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-10 offset-md-1">
        <div class="card">
            <div class="card-header">
                <h2>Add Question to: {{ exam.title }}</h2>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="{{ question_form.text.id_for_label }}" class="form-label">Question text</label>
                        {{ question_form.text }}
                        {% if question_form.text.errors %}
                            <div class="text-danger">{{ question_form.text.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <h4 class="mt-4 mb-3">Answer options</h4>
                    <div class="alert alert-info">
                        Check the "Is correct" box on the option that is the correct answer.
                    </div>
                    
                    {{ formset.management_form }}
                    <div id="options-container">
                        {% for choice_form in formset %}
                            <div class="card mb-3">
                                <div class="card-body">
                                    <div class="row">
                                        <div class="col-md-9">
                                            <label class="form-label">Option {{ forloop.counter }}</label>
                                            {{ choice_form.text }}
                                        </div>
                                        <div class="col-md-3">
                                            <div class="form-check mt-2">
                                                {{ choice_form.is_correct }}
                                                <label class="form-check-label" for="{{ choice_form.is_correct.id_for_label }}">
                                                    Is correct
                                                </label>
                                            </div>
                                        </div>
                                    </div>
                                    {{ choice_form.id }}
                                </div>
                            </div>
                        {% endfor %}
                    </div>
                    
                    <div class="d-flex justify-content-between mt-4">
                        <a href="{% url 'exam_detail' exam.id %}" class="btn btn-secondary">Cancel</a>
                        <div>
                            <button type="submit" name="add_another" class="btn btn-info">Save and add another</button>
                            <button type="submit" class="btn btn-primary">Save and finish</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script>
    // Script to ensure only one option is marked as correct
    document.addEventListener('DOMContentLoaded', function() {
        const checkboxes = document.querySelectorAll('input[type=checkbox]');
        
        checkboxes.forEach(function(checkbox) {
            checkbox.addEventListener('change', function() {
                if (this.checked) {
                    // Uncheck other options
                    checkboxes.forEach(function(otherCheckbox) {
                        if (otherCheckbox !== checkbox) {
                            otherCheckbox.checked = false;
                        }
                    });
                }
            });
        });
    });
</script>
{% endblock %}
```

## Step 10: Run the Server 🚀

```bash
python3 manage.py runserver
```

Now you can access:
- List of exams: http://127.0.0.1:8000/
- Create exam: http://127.0.0.1:8000/exam/create/

## Step 11: Register Models in Admin (optional) 👨‍💼

Edit `quiz/admin.py`:

```python
from django.contrib import admin
from .models import Exam, Question, Choice

class ChoiceInline(admin.TabularInline):
    """Inline admin for choices"""
    model = Choice
    extra = 4

class QuestionInline(admin.StackedInline):
    """Inline admin for questions"""
    model = Question
    extra = 1

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    """Admin configuration for exams"""
    list_display = ('title', 'created_date')
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Admin configuration for questions"""
    list_display = ('text', 'exam')
    inlines = [ChoiceInline]
```

## Application Workflow 🔄

1. **Create an exam** 📝:
   - Access the main page and click "Create Exam"
   - Complete the title and description
   - Click "Continue"

2. **Add questions to the exam** ❓:
   - After creating the exam, you'll be redirected to the question form
   - Write the question text
   - Add the answer options
   - Check the "Is correct" box on the option that is the correct answer
   - Click "Save and add another" to add more questions or "Save and finish" to complete

3. **View the list of exams** 📋:
   - Access the main page to see all exams
   - Click "View Details" to explore a specific exam

4. **View exam details** 🔍:
   - Review all the questions in the exam
   - Expand each question to see its options
   - The correct options are highlighted in green

## Conclusions 🎓

In this guide, you've learned how to:

1. **Create a basic Django application** with models for exams, questions, and options.

2. **Implement relationships between models** using ForeignKey to establish connections between exams, questions, and options.

3. **Create forms** for data entry, including formsets to handle multiple answer options.

4. **Develop views** for the three main functionalities:
   - List of exams
   - Exam details
   - Creating exams and questions

5. **Design templates** using Bootstrap for a simple but functional interface.

This application demonstrates how Django facilitates the creation of web applications with related data models. The concepts learned here can be applied to more complex projects, adding more functionalities as needed.

## Suggestions to Expand the Project 🚀

If you want to expand this application, here are some interesting challenges:

1. **Improve exam management** 📊:
   - Implement editing of exams and questions
   - Add functionality to delete questions
   - Allow reordering questions using drag-and-drop

2. **Create a game system** 🎮:
   - Develop a view to "play" the exam
   - Implement a timer to limit response time
   - Calculate and display scores based on correct answers
   - Generate a summary of results upon completion

3. **Add social features** 👥:
   - Implement a user system
   - Allow sharing exams with other users
   - Create score rankings

## Additional Application Proposals 💡

To continue practicing with Django, I propose developing these complementary applications:

### 1. Categories Application (categories) 🏷️

Create a separate application to manage exam categories:

```bash
python3 manage.py startapp categories
```

This application could:
- Define a `Category` model with fields like name, description, and icon
- Relate categories to exams (many-to-many relationship)
- Allow filtering exams by category
- Show statistics of exams by category

### 2. Statistics Application (stats) 📈

Develop an application to analyze performance:

```bash
python3 manage.py startapp stats
```

This application could:
- Record user attempts on exams
- Calculate statistics such as percentage of correct answers, average time, etc.
- Generate performance graphs
- Identify questions with highest failure rates

Implementing these applications will allow you to practice more advanced Django concepts such as relationships between models, complex queries, and data management across multiple applications.