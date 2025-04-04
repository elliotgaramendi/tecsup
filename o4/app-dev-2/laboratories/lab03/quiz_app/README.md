# 📝 Quiz App - Aplicación de Cuestionarios en Django

Una aplicación simple para crear y gestionar cuestionarios tipo quiz, desarrollada con Django.

## 📋 Características

- Crear exámenes con título y descripción
- Añadir preguntas con múltiples opciones
- Especificar la respuesta correcta para cada pregunta
- Visualizar exámenes y sus preguntas con detalle
- Interfaz intuitiva basada en Bootstrap

## 🔧 Tecnologías

- Python 3.x
- Django
- Bootstrap 5
- SQLite (por defecto)

## 💻 Instalación y Configuración

1. **Clonar el repositorio**
```bash
git clone https://github.com/yourusername/quiz-app.git
cd quiz-app
```

2. **Crear y activar entorno virtual**
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
cd src
pip install -r requirements.txt
```

4. **Aplicar migraciones**
```bash
python3 manage.py migrate
```

5. **Crear superusuario (opcional)**
```bash
python3 manage.py createsuperuser
```

6. **Iniciar servidor de desarrollo**
```bash
python3 manage.py runserver
```

## 🚀 Uso

1. **Crear un examen**
   - Accede a la página principal y haz clic en "Crear Examen"
   - Completa el título y descripción
   - Haz clic en "Continuar"

2. **Añadir preguntas**
   - Escribe el texto de la pregunta
   - Añade las opciones de respuesta (al menos 2)
   - Marca la opción correcta
   - Guarda la pregunta

3. **Ver exámenes**
   - La página principal muestra todos los exámenes disponibles
   - Cada examen muestra su título, descripción y número de preguntas

4. **Ver detalle de un examen**
   - Haz clic en "Ver Detalles" en cualquier examen
   - Aquí puedes ver todas las preguntas y sus opciones
   - Las respuestas correctas están resaltadas

## 📁 Estructura del Proyecto

```
quiz_app/
├── .gitignore
├── venv/
└── src/
    ├── config/             # Configuración del proyecto
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── quiz/               # Aplicación principal
    │   ├── models.py       # Modelos: Exam, Question, Choice
    │   ├── forms.py        # Formularios
    │   ├── views.py        # Lógica de vistas
    │   ├── urls.py         # Configuración de URLs
    │   ├── templates/      # Plantillas HTML
    │   └── ...
    ├── manage.py           # Script de gestión de Django
    └── requirements.txt    # Dependencias
```

## 🛠️ Modelos

La aplicación se basa en tres modelos principales:

- **Exam**: Representa un cuestionario con título y descripción
- **Question**: Representa una pregunta individual asociada a un examen
- **Choice**: Representa una opción de respuesta para una pregunta

## 🔄 Flujo de la Aplicación

1. El usuario crea un examen nuevo
2. El sistema redirige al usuario a añadir preguntas
3. Para cada pregunta, el usuario añade opciones y marca la correcta
4. El examen queda disponible en la lista para ser consultado

## ⚙️ Personalización

Puedes personalizar la aplicación modificando:

- Los modelos en `quiz/models.py` para añadir campos adicionales
- Las plantillas en `quiz/templates/` para cambiar el diseño
- Los estilos mediante CSS o clases de Bootstrap

## 🔜 Futuras Mejoras

- Sistema para jugar los exámenes y obtener puntuación
- Edición y eliminación de preguntas
- Categorización de exámenes
- Sistema de usuarios y gestión de permisos
- Estadísticas de resultados

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE.md para más detalles.

## 👨‍💻 Autor

Tu Nombre - [tu-email@ejemplo.com](mailto:tu-email@ejemplo.com)

---

Desarrollado como parte del curso "Desarrollo de Aplicaciones Empresariales"