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