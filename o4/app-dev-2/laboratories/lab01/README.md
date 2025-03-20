# Django 5 Project Setup Guide

This guide walks through setting up a Django 5 project with a modern, organized structure optimized for scalability.

## Project Structure

```
my_django_project/
├── README.md
├── venv/
└── src/
    ├── manage.py
    ├── requirements.txt
    ├── config/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── core/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations/
        ├── models.py
        ├── templates/
        │   ├── base.html
        │   └── core/
        │       └── item_list.html
        ├── tests.py
        ├── urls.py
        └── views.py
```

## Step-by-Step Setup Guide

### 1. Initial Setup

```bash
# Create main project directory
mkdir my_django_project
cd my_django_project

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

### 3. Create the project with separate configuration

```bash
# Being in the src folder
django-admin startproject config .
```

This creates:
- `manage.py` in the `src/` directory
- A `config/` folder with `settings.py`, `urls.py`, etc.

### 4. Create the core application

```bash
# Being in the src folder
python3 manage.py startapp core
```

### 5. Register the application in settings.py

Edit `src/config/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttents',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Our application
]
```

### 6. Define a basic model

In `src/core/models.py`:

```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

### 7. Create and apply migrations

```bash
# Being in src
python3 manage.py makemigrations
python3 manage.py migrate
```

### 8. Create a basic view

In `src/core/views.py`:

```python
from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'core/item_list.html', {'items': items})
```

### 9. Configure URLs

In `src/config/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

Create `src/core/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
]
```

### 10. Create directories for templates

```bash
# Being in /src
mkdir -p core/templates/core
```

### 11. Create base template

Create `src/core/templates/base.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Django Project</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <header>
        <h1>My Django Project</h1>
    </header>
    <main>
        {% block content %}
        {% endblock %}
    </main>
    <footer>
        <p>Developed with Django</p>
    </footer>
</body>
</html>
```

### 12. Create list template

Create `src/core/templates/core/item_list.html`:

```html
{% extends "base.html" %}

{% block content %}
  <h1>Items</h1>
  <ul>
    {% for item in items %}
      <li>{{ item.name }} - {{ item.created_at|date:"d/m/Y" }}</li>
    {% empty %}
      <li>No items available.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

### 13. Register model in admin

In `src/core/admin.py`:

```python
from django.contrib import admin
from .models import Item

admin.site.register(Item)
```

### 14. Create superuser for admin access

```bash
python3 manage.py createsuperuser
# Use 'admin' as username and 'admin' as password for testing
# Email: you can leave it blank for development
```

### 15. Run development server

```bash
# From src
python3 manage.py runserver
```

### 16. Access the admin panel

1. Open your browser and go to http://127.0.0.1:8000/admin/
2. Log in with the admin user and password you created

### 17. Create test items

1. In the admin panel, click on "Items" under the "Core" section
2. Click on "ADD ITEM" in the top right corner
3. Complete the form:
   - Name: "First Item"
   - Description: "This is a test description"
4. Click "SAVE"
5. Create another item following the same steps

### 18. View the main page with the items

1. Go to http://127.0.0.1:8000/ in your browser
2. You should see the list of items you just created

### 19. Generate requirements.txt file

```bash
# From src directory
pip3 freeze > requirements.txt
```

### 20. Create a README.md file

Create a file named `README.md` in the root directory (`my_django_project/`):

```bash
# Navigate back to root project directory
cd ..
touch README.md
```

## Sample README.md

```markdown
# 🚀 My Django Project

A modern Django web application with a clean, organized structure.

## 📋 Overview

This project follows a custom structure:
- `src/`: Main code directory
  - `config/`: Project configuration
  - `core/`: Main application
- `venv/`: Virtual environment (not tracked in git)

## ✨ Features

- 📱 Clean and organized Django 5 structure
- 🛠️ Separation of settings and application code
- 📦 Ready to use with frontend frameworks
- 🔒 Admin interface for content management

## 🔧 Installation

1. Clone this repository
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   cd src
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python3 manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python3 manage.py createsuperuser
   ```

## 🚀 Running the Project

```bash
cd src
python3 manage.py runserver
```

Access the site at http://127.0.0.1:8000/ and admin at http://127.0.0.1:8000/admin/

## 🛠️ Development

- Add models to `core/models.py`
- Create views in `core/views.py`
- Add URL patterns in `core/urls.py`
- Create templates in `core/templates/`

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Your Name

---

Built with ❤️ using Django 5