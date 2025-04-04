# Guía: Aplicación Simple de Cuestionarios con Django

Esta guía te mostrará cómo crear una aplicación básica de cuestionarios con Django, con funcionalidades para crear exámenes, agregar preguntas y especificar respuestas correctas.

## Estructura de la Aplicación

Crearemos 3 rutas principales:
- Lista de exámenes
- Detalle de un examen con sus preguntas
- Formulario para crear exámenes y preguntas

## Paso 1: Configuración del Entorno

```bash
# Crear directorio del proyecto
mkdir quiz_app
cd quiz_app

# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Crear directorio src (estructura similar a proyectos frontend)
mkdir src
cd src

# Instalar Django
pip3 install django

# Crear un archivo requirements.txt
pip3 freeze > requirements.txt
```

**Nota**: Si estás usando Git, crea un archivo `.gitignore` en la raíz del proyecto:

```bash
# Volver a la raíz del proyecto
cd ..

# Crear archivo .gitignore
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

Esto evitará versionar archivos innecesarios como caché de Python, base de datos SQLite y el entorno virtual.

## Paso 2: Crear el Proyecto Django

```bash
# Asegúrate de estar en el directorio src
cd src

# Crear proyecto
django-admin startproject config .

# Crear aplicación
python3 manage.py startapp quiz
```

## Paso 3: Configuración Básica

Editar `config/settings.py` para incluir la app:

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

## Paso 4: Definir los Modelos

Editar `quiz/models.py`:

```python
from django.db import models

class Exam(models.Model):
    """Model for exams"""
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(blank=True, verbose_name="Descripción")
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_question_count(self):
        """Returns the number of questions in this exam"""
        return self.questions.count()

class Question(models.Model):
    """Model for questions"""
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name="Texto de la pregunta")
    
    def __str__(self):
        return self.text[:50]

class Choice(models.Model):
    """Model for answer choices"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200, verbose_name="Texto")
    is_correct = models.BooleanField(default=False, verbose_name="Es correcta")
    
    def __str__(self):
        return self.text
```

## Paso 5: Migrar la Base de Datos

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

**Nota**: Recuerda que los archivos de migración (en `migrations/`) deben versionarse, pero el archivo `db.sqlite3` debe excluirse del control de versiones (ya está en el `.gitignore` que creamos).

## Paso 6: Crear Formularios

Crear archivo `quiz/forms.py`:

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

# Crear formset para opciones
ChoiceFormSet = forms.inlineformset_factory(
    Question, Choice, form=ChoiceForm, extra=4, can_delete=False
)
```

## Paso 7: Crear Vistas

Editar `quiz/views.py`:

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
            messages.success(request, 'Examen creado correctamente.')
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
                        messages.warning(request, 'Debe haber exactamente una respuesta correcta.')
                    else:
                        messages.success(request, 'Pregunta añadida correctamente.')
                        
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

## Paso 8: Configurar URLs

Crear `quiz/urls.py`:

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

Editar `config/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),
]
```

## Paso 9: Crear Plantillas

Crear estructura de directorios:

```bash
mkdir -p quiz/templates/quiz
```

### Plantilla Base (quiz/templates/base.html)

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Aplicación de Cuestionarios{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light mb-4">
        <div class="container">
            <a class="navbar-brand" href="{% url 'exam_list' %}">Cuestionarios</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'exam_list' %}">Exámenes</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'exam_create' %}">Crear Examen</a>
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

### Lista de Exámenes (quiz/templates/quiz/exam_list.html)

```html
{% extends "base.html" %}

{% block title %}Exámenes{% endblock %}

{% block content %}
<div class="row mb-4">
    <div class="col-md-6">
        <h1>Exámenes Disponibles</h1>
    </div>
    <div class="col-md-6 text-end">
        <a href="{% url 'exam_create' %}" class="btn btn-primary">Crear Examen</a>
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
                        <p class="text-muted">Preguntas: {{ exam.get_question_count }}</p>
                        <a href="{% url 'exam_detail' exam.id %}" class="btn btn-primary">Ver Detalles</a>
                    </div>
                </div>
            </div>
        {% endfor %}
    {% else %}
        <div class="col-12">
            <div class="alert alert-info">
                No hay exámenes disponibles.
                <a href="{% url 'exam_create' %}">Crea el primero</a>
            </div>
        </div>
    {% endif %}
</div>
{% endblock %}
```

### Detalle de Examen (quiz/templates/quiz/exam_detail.html)

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
        <a href="{% url 'question_create' exam.id %}" class="btn btn-primary">Añadir Pregunta</a>
    </div>
</div>

<div class="mb-4">
    <h2>Preguntas</h2>
    
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
                                        {{ choice.text }} {% if choice.is_correct %}<span class="badge bg-success">Correcta</span>{% endif %}
                                    </li>
                                {% empty %}
                                    <li class="list-group-item">No hay opciones para esta pregunta.</li>
                                {% endfor %}
                            </ul>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    {% else %}
        <div class="alert alert-info">
            Este examen no tiene preguntas todavía.
            <a href="{% url 'question_create' exam.id %}">Añade la primera pregunta</a>
        </div>
    {% endif %}
</div>

<div>
    <a href="{% url 'exam_list' %}" class="btn btn-secondary">Volver a la lista</a>
</div>
{% endblock %}
```

### Formulario de Examen (quiz/templates/quiz/exam_form.html)

```html
{% extends "base.html" %}

{% block title %}Crear Examen{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-8 offset-md-2">
        <div class="card">
            <div class="card-header">
                <h2>Crear Nuevo Examen</h2>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="{{ form.title.id_for_label }}" class="form-label">Título</label>
                        {{ form.title }}
                        {% if form.title.errors %}
                            <div class="text-danger">{{ form.title.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="mb-3">
                        <label for="{{ form.description.id_for_label }}" class="form-label">Descripción</label>
                        {{ form.description }}
                        {% if form.description.errors %}
                            <div class="text-danger">{{ form.description.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <div class="d-flex justify-content-between">
                        <a href="{% url 'exam_list' %}" class="btn btn-secondary">Cancelar</a>
                        <button type="submit" class="btn btn-primary">Continuar</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### Formulario de Pregunta (quiz/templates/quiz/question_form.html)

```html
{% extends "base.html" %}

{% block title %}Añadir Pregunta{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-10 offset-md-1">
        <div class="card">
            <div class="card-header">
                <h2>Añadir Pregunta a: {{ exam.title }}</h2>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="{{ question_form.text.id_for_label }}" class="form-label">Texto de la pregunta</label>
                        {{ question_form.text }}
                        {% if question_form.text.errors %}
                            <div class="text-danger">{{ question_form.text.errors }}</div>
                        {% endif %}
                    </div>
                    
                    <h4 class="mt-4 mb-3">Opciones de respuesta</h4>
                    <div class="alert alert-info">
                        Marca la casilla "Es correcta" en la opción que sea la respuesta correcta.
                    </div>
                    
                    {{ formset.management_form }}
                    <div id="options-container">
                        {% for choice_form in formset %}
                            <div class="card mb-3">
                                <div class="card-body">
                                    <div class="row">
                                        <div class="col-md-9">
                                            <label class="form-label">Opción {{ forloop.counter }}</label>
                                            {{ choice_form.text }}
                                        </div>
                                        <div class="col-md-3">
                                            <div class="form-check mt-2">
                                                {{ choice_form.is_correct }}
                                                <label class="form-check-label" for="{{ choice_form.is_correct.id_for_label }}">
                                                    Es correcta
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
                        <a href="{% url 'exam_detail' exam.id %}" class="btn btn-secondary">Cancelar</a>
                        <div>
                            <button type="submit" name="add_another" class="btn btn-info">Guardar y añadir otra</button>
                            <button type="submit" class="btn btn-primary">Guardar y terminar</button>
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
    // Script para asegurar que solo una opción sea marcada como correcta
    document.addEventListener('DOMContentLoaded', function() {
        const checkboxes = document.querySelectorAll('input[type=checkbox]');
        
        checkboxes.forEach(function(checkbox) {
            checkbox.addEventListener('change', function() {
                if (this.checked) {
                    // Desmarcar las demás opciones
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

## Paso 10: Ejecutar el Servidor

```bash
python3 manage.py runserver
```

Ahora puedes acceder a:
- Lista de exámenes: http://127.0.0.1:8000/
- Crear examen: http://127.0.0.1:8000/exam/create/

## Paso 11: Registrar los Modelos en el Admin (opcional)

Editar `quiz/admin.py`:

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

## Flujo de Trabajo de la Aplicación

1. **Crear un examen**:
   - Accede a la página principal y haz clic en "Crear Examen"
   - Completa el título y descripción
   - Haz clic en "Continuar"

2. **Añadir preguntas al examen**:
   - Después de crear el examen, serás redirigido al formulario de preguntas
   - Escribe el texto de la pregunta
   - Agrega las opciones de respuesta
   - Marca la casilla "Es correcta" en la opción que sea la respuesta correcta
   - Haz clic en "Guardar y añadir otra" para añadir más preguntas o "Guardar y terminar" para finalizar

3. **Ver la lista de exámenes**:
   - Accede a la página principal para ver todos los exámenes
   - Haz clic en "Ver Detalles" para explorar un examen específico

4. **Ver detalle de un examen**:
   - Revisa todas las preguntas del examen
   - Expande cada pregunta para ver sus opciones
   - Las opciones correctas se destacan en verde

## Conclusiones

En esta guía, has aprendido a:

1. **Crear una aplicación Django básica** con modelos para exámenes, preguntas y opciones.

2. **Implementar relaciones entre modelos** usando ForeignKey para establecer conexiones entre exámenes, preguntas y opciones.

3. **Crear formularios** para la entrada de datos, incluyendo formsets para manejar múltiples opciones de respuesta.

4. **Desarrollar vistas** para las tres funcionalidades principales:
   - Listado de exámenes
   - Detalle de un examen
   - Creación de exámenes y preguntas

5. **Diseñar plantillas** utilizando Bootstrap para una interfaz sencilla pero funcional.

Esta aplicación demuestra cómo Django facilita la creación de aplicaciones web con modelos de datos relacionados. Los conceptos aprendidos aquí pueden aplicarse a proyectos más complejos, añadiendo más funcionalidades según sea necesario.

## Sugerencias para Ampliar el Proyecto

Si deseas ampliar esta aplicación, aquí hay algunos retos interesantes:

1. **Mejorar la gestión de exámenes**:
   - Implementar la edición de exámenes y preguntas
   - Añadir funcionalidad para eliminar preguntas
   - Permitir reordenar las preguntas mediante drag-and-drop

2. **Crear un sistema de juego**:
   - Desarrollar una vista para "jugar" el examen
   - Implementar un temporizador para limitar el tiempo de respuesta
   - Calcular y mostrar puntuaciones basadas en respuestas correctas
   - Generar un resumen de resultados al finalizar

3. **Añadir características sociales**:
   - Implementar un sistema de usuarios
   - Permitir compartir exámenes con otros usuarios
   - Crear rankings de puntuaciones

## Propuestas de Aplicaciones Adicionales

Para seguir practicando con Django, te propongo desarrollar estas aplicaciones complementarias:

### 1. Aplicación de Categorías (categories)

Crea una aplicación separada para gestionar categorías de exámenes:

```bash
python3 manage.py startapp categories
```

Esta aplicación podría:
- Definir un modelo `Category` con campos como nombre, descripción e icono
- Relacionar categorías con exámenes (relación muchos a muchos)
- Permitir filtrar exámenes por categoría
- Mostrar estadísticas de exámenes por categoría

### 2. Aplicación de Estadísticas (stats)

Desarrolla una aplicación para analizar el rendimiento:

```bash
python3 manage.py startapp stats
```

Esta aplicación podría:
- Registrar los intentos de los usuarios en los exámenes
- Calcular estadísticas como porcentaje de aciertos, tiempo promedio, etc.
- Generar gráficos de rendimiento
- Identificar preguntas con mayor índice de fallos

Implementar estas aplicaciones te permitirá practicar conceptos más avanzados de Django como relaciones entre modelos, queries complejas y gestión de datos entre múltiples aplicaciones.