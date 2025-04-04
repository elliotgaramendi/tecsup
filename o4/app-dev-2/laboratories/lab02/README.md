# 🚀 Django Task Manager - Practical Guide

This guide will walk you through creating a Task Manager application using Django, applying the workflow concepts from the presentation. We'll create two main views: one with a form to register tasks and another to read/list them.

## 📋 Project Overview

We'll build a Task Manager with these features:
- Task creation with title, description, due date, and priority
- Task listing with filtering options
- Structured according to Django's MVT (Model-View-Template) pattern

## 🛠️ Setup and Environment Configuration

### 1. Create project directory and virtual environment

```bash
# Create main project directory
mkdir task_manager
cd task_manager

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Create src directory
mkdir src
cd src
```

### 2. Install Django

```bash
pip3 install django
```

### 3. Create a requirements file

```bash
pip3 freeze > requirements.txt
```

### 4. Create the Django project

```bash
# Being in the src folder
django-admin startproject config .
```

### 5. Create the tasks application

```bash
python3 manage.py startapp tasks
```

### 6. Register the application in settings.py

Edit `src/config/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',  # Our task manager application
]
```

## 📝 Model Definition

Let's define our Task model in `src/tasks/models.py`:

```python
from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='pending'
    )
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-created_date']
```

## 🗄️ Create and Apply Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## 🧩 Create Forms

Create a new file `src/tasks/forms.py`:

```python
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'status']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
```

## 🖥️ Create Views

Edit `src/tasks/views.py`:

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    
    # Handle filtering
    status_filter = request.GET.get('status')
    priority_filter = request.GET.get('priority')
    
    if status_filter and status_filter != 'all':
        tasks = tasks.filter(status=status_filter)
    
    if priority_filter and priority_filter != 'all':
        tasks = tasks.filter(priority=priority_filter)
    
    context = {
        'tasks': tasks,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
    }
    
    return render(request, 'tasks/task_list.html', context)

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
```

## 🔗 Configure URLs

First, edit `src/config/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]
```

Next, create a new file `src/tasks/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
```

## 🎨 Create Templates

First, create the necessary directory structure:

```bash
mkdir -p tasks/templates/tasks
```

### Create base template

Create `src/tasks/templates/base.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Manager</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .priority-high { background-color: #ffeeee; }
        .priority-medium { background-color: #ffffee; }
        .priority-low { background-color: #eeffee; }
        .task-completed { text-decoration: line-through; color: #888; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div class="container">
            <a class="navbar-brand" href="{% url 'task_list' %}">📝 Task Manager</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'task_list' %}">Tasks</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'task_create' %}">New Task</a>
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

        {% block content %}
        {% endblock %}
    </div>

    <footer class="mt-5 py-3 bg-light text-center">
        <div class="container">
            <p class="text-muted">Task Manager - Built with Django</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### Create task list template

Create `src/tasks/templates/tasks/task_list.html`:

```html
{% extends "base.html" %}

{% block content %}
    <div class="row">
        <div class="col-md-8">
            <h2>My Tasks</h2>
        </div>
        <div class="col-md-4 text-end">
            <a href="{% url 'task_create' %}" class="btn btn-primary">
                <i class="bi bi-plus-circle"></i> Add New Task
            </a>
        </div>
    </div>

    <div class="row mt-3 mb-4">
        <div class="col">
            <form method="get" class="row g-3">
                <div class="col-md-5">
                    <label class="form-label">Status:</label>
                    <select name="status" class="form-select" onchange="this.form.submit()">
                        <option value="all" {% if status_filter == 'all' or not status_filter %}selected{% endif %}>All</option>
                        <option value="pending" {% if status_filter == 'pending' %}selected{% endif %}>Pending</option>
                        <option value="in_progress" {% if status_filter == 'in_progress' %}selected{% endif %}>In Progress</option>
                        <option value="completed" {% if status_filter == 'completed' %}selected{% endif %}>Completed</option>
                    </select>
                </div>
                <div class="col-md-5">
                    <label class="form-label">Priority:</label>
                    <select name="priority" class="form-select" onchange="this.form.submit()">
                        <option value="all" {% if priority_filter == 'all' or not priority_filter %}selected{% endif %}>All</option>
                        <option value="high" {% if priority_filter == 'high' %}selected{% endif %}>High</option>
                        <option value="medium" {% if priority_filter == 'medium' %}selected{% endif %}>Medium</option>
                        <option value="low" {% if priority_filter == 'low' %}selected{% endif %}>Low</option>
                    </select>
                </div>
                <div class="col-md-2 d-flex align-items-end">
                    <button type="submit" class="btn btn-secondary w-100">Filter</button>
                </div>
            </form>
        </div>
    </div>

    {% if tasks %}
        <div class="table-responsive">
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Priority</th>
                        <th>Status</th>
                        <th>Due Date</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {% for task in tasks %}
                        <tr class="{% if task.status == 'completed' %}task-completed{% else %}priority-{{ task.priority }}{% endif %}">
                            <td>{{ task.title }}</td>
                            <td>
                                {% if task.priority == 'high' %}
                                    <span class="badge bg-danger">High</span>
                                {% elif task.priority == 'medium' %}
                                    <span class="badge bg-warning text-dark">Medium</span>
                                {% else %}
                                    <span class="badge bg-success">Low</span>
                                {% endif %}
                            </td>
                            <td>
                                {% if task.status == 'pending' %}
                                    <span class="badge bg-secondary">Pending</span>
                                {% elif task.status == 'in_progress' %}
                                    <span class="badge bg-primary">In Progress</span>
                                {% else %}
                                    <span class="badge bg-success">Completed</span>
                                {% endif %}
                            </td>
                            <td>{% if task.due_date %}{{ task.due_date }}{% else %}-{% endif %}</td>
                            <td>
                                <div class="btn-group btn-group-sm">
                                    <a href="{% url 'task_update' task.id %}" class="btn btn-outline-primary">Edit</a>
                                    <a href="{% url 'task_delete' task.id %}" class="btn btn-outline-danger">Delete</a>
                                </div>
                            </td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    {% else %}
        <div class="alert alert-info">
            No tasks found. <a href="{% url 'task_create' %}">Create your first task</a>
        </div>
    {% endif %}
{% endblock %}
```

### Create task form template

Create `src/tasks/templates/tasks/task_form.html`:

```html
{% extends "base.html" %}

{% block content %}
    <div class="row">
        <div class="col-md-8 offset-md-2">
            <div class="card">
                <div class="card-header bg-primary text-white">
                    <h3 class="card-title">
                        {% if form.instance.id %}
                            Edit Task
                        {% else %}
                            Create New Task
                        {% endif %}
                    </h3>
                </div>
                <div class="card-body">
                    <form method="post" novalidate>
                        {% csrf_token %}
                        
                        <div class="mb-3">
                            <label for="{{ form.title.id_for_label }}" class="form-label">Title</label>
                            {{ form.title }}
                            {% if form.title.errors %}
                                <div class="text-danger">
                                    {{ form.title.errors }}
                                </div>
                            {% endif %}
                        </div>
                        
                        <div class="mb-3">
                            <label for="{{ form.description.id_for_label }}" class="form-label">Description</label>
                            {{ form.description }}
                            {% if form.description.errors %}
                                <div class="text-danger">
                                    {{ form.description.errors }}
                                </div>
                            {% endif %}
                        </div>
                        
                        <div class="row">
                            <div class="col-md-4 mb-3">
                                <label for="{{ form.due_date.id_for_label }}" class="form-label">Due Date</label>
                                {{ form.due_date }}
                                {% if form.due_date.errors %}
                                    <div class="text-danger">
                                        {{ form.due_date.errors }}
                                    </div>
                                {% endif %}
                            </div>
                            
                            <div class="col-md-4 mb-3">
                                <label for="{{ form.priority.id_for_label }}" class="form-label">Priority</label>
                                {{ form.priority }}
                                {% if form.priority.errors %}
                                    <div class="text-danger">
                                        {{ form.priority.errors }}
                                    </div>
                                {% endif %}
                            </div>
                            
                            <div class="col-md-4 mb-3">
                                <label for="{{ form.status.id_for_label }}" class="form-label">Status</label>
                                {{ form.status }}
                                {% if form.status.errors %}
                                    <div class="text-danger">
                                        {{ form.status.errors }}
                                    </div>
                                {% endif %}
                            </div>
                        </div>
                        
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                            <a href="{% url 'task_list' %}" class="btn btn-secondary me-md-2">Cancel</a>
                            <button type="submit" class="btn btn-primary">
                                {% if form.instance.id %}
                                    Update Task
                                {% else %}
                                    Create Task
                                {% endif %}
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
{% endblock %}
```

### Create task delete confirmation template

Create `src/tasks/templates/tasks/task_confirm_delete.html`:

```html
{% extends "base.html" %}

{% block content %}
    <div class="row">
        <div class="col-md-6 offset-md-3">
            <div class="card">
                <div class="card-header bg-danger text-white">
                    <h3 class="card-title">Delete Task</h3>
                </div>
                <div class="card-body">
                    <p>Are you sure you want to delete the task "{{ task.title }}"?</p>
                    <form method="post">
                        {% csrf_token %}
                        <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                            <a href="{% url 'task_list' %}" class="btn btn-secondary me-md-2">Cancel</a>
                            <button type="submit" class="btn btn-danger">Yes, Delete</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
{% endblock %}
```

## 🧩 Register Model in Admin

Edit `src/tasks/admin.py`:

```python
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status', 'due_date', 'created_date')
    list_filter = ('status', 'priority')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_date'
```

## 🚀 Run the Development Server

```bash
python3 manage.py createsuperuser
# Follow the prompts to create an admin user

python3 manage.py runserver
```

Now you can access:
- The task list at http://127.0.0.1:8000/
- The task creation form at http://127.0.0.1:8000/task/new/
- The admin interface at http://127.0.0.1:8000/admin/

## 🔄 Django Workflow Applied

This project follows the Django workflow as described in the presentation:

1. **Configuration of the environment**
   - Created virtual environment
   - Installed Django
   - Set up project structure

2. **Design of Data Model**
   - Created Task model with relevant fields
   - Applied migrations to create database schema

3. **Creation of Views**
   - Implemented list, create, update, and delete views for tasks

4. **Definition of URLs**
   - Configured URL patterns to map to appropriate views

5. **Creation of Templates**
   - Built HTML templates for displaying task list and forms

6. **Form Handling**
   - Created a TaskForm using Django's ModelForm

7. **Business Logic Implementation**
   - Added filtering functionality
   - Implemented CRUD operations

8. **Testing**
   - The server is ready for manual testing

## 📈 Next Steps

To further enhance your Task Manager:

1. **Add User Authentication**
   - Allow users to register and log in
   - Associate tasks with specific users

2. **Add Task Categories**
   - Create a Category model
   - Allow tasks to be assigned to categories

3. **Implement Task Search**
   - Add a search box to find tasks by keywords

4. **Add Due Date Reminders**
   - Email notifications for approaching deadlines

5. **Implement Task Comments**
   - Allow users to add comments to tasks

6. **Research Challenge: Create an Authors App**
   - Investigate how to create a separate Django app for authors/users
   - Research how to create relationships between authors and tasks
   - Explore Django's User model extension options
   - Design an interface for assigning tasks to specific authors
   - *This is an excellent exercise to understand model relationships (ForeignKey) and app separation*

7. **Research Challenge: Implement a Tags System (Like Trello)**
   - Research how to create a tags system similar to Trello
   - Explore Django's ManyToManyField for creating tag relationships
   - Design a color-coded tag system for visual organization
   - Implement filtering by tags
   - *This exercise will help understand many-to-many relationships and advanced filtering*

## 📝 Conclusion

You've now created a functional Task Manager application using Django, following the workflow concepts from the presentation. This demonstrates the practical application of Django's MVT (Model-View-Template) pattern and showcases how Django's components work together to create a complete web application.

---

## 📚 References

- Django official documentation: https://docs.djangoproject.com/
- Django Forms documentation: https://docs.djangoproject.com/en/stable/topics/forms/
- Bootstrap documentation: https://getbootstrap.com/docs/5.3/