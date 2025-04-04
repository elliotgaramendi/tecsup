# 📋 Django Task Manager

A modern task management application built with Django.

![Django](https://img.shields.io/badge/Django-5.1-green.svg)
![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)

## ✨ Features

- 🔄 Complete task lifecycle management (create, read, update, delete)
- 🏷️ Task prioritization (Low, Medium, High)
- 📊 Status tracking (Pending, In Progress, Completed)
- 📅 Due date assignment
- 🔍 Filtering by priority and status
- 👑 Admin interface for data management

## 🚀 Installation

1. Clone this repository
```bash
git clone https://github.com/yourusername/django-task-manager.git
cd django-task-manager
```

2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
cd src
pip3 install -r requirements.txt
```

4. Apply migrations
```bash
python3 manage.py migrate
```

5. Create a superuser (admin)
```bash
python3 manage.py createsuperuser
```

## 💻 Usage

1. Start the development server:
```bash
python3 manage.py runserver
```

2. Open your browser and navigate to:
   - Main application: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## 🧩 Project Structure

```
django_task_manager/
├── venv/                  # Virtual environment (not in repository)
└── src/                   # Source code
    ├── config/            # Project configuration
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── tasks/             # Tasks application
    │   ├── models.py      # Task data model
    │   ├── views.py       # View functions
    │   ├── forms.py       # Form definitions
    │   ├── urls.py        # URL routing
    │   ├── admin.py       # Admin configuration
    │   └── templates/     # HTML templates
    ├── manage.py          # Django management script
    └── requirements.txt   # Project dependencies
```

## 🔄 Workflow

This project follows Django's MVT (Model-View-Template) pattern:
1. **Models**: Define data structure
2. **Views**: Process requests and return responses
3. **Templates**: Define how data is displayed
4. **URLs**: Connect URLs to views

## 🎯 Future Enhancements

- [ ] User authentication and task assignment
- [ ] Task categories/tags
- [ ] Search functionality
- [ ] Due date notifications
- [ ] Task comments
- [ ] Mobile-responsive design improvements

## 🛠️ Technologies Used

- [Django](https://www.djangoproject.com/) - Web framework
- [Bootstrap](https://getbootstrap.com/) - Frontend framework
- [SQLite](https://www.sqlite.org/) - Database (development)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Made with ❤️ by Elliot Garamendi