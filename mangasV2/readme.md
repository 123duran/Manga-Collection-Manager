# 📚 Manga Collection Manager

A web application built with Django to manage a personal manga collection. Features include adding, editing, viewing, and deleting mangas and chapters, tracking ownership, and responsive design with Bootstrap.

---

## 🚀 Features

- ✅ User authentication (login required for managing content)
- 📖 Add, edit, and delete mangas
- 📄 Add chapters to mangas and mark them as owned or not
- 📊 Progress bar showing percentage of owned chapters
- 🖼️ Support for manga cover images (via URL)
- 🔍 Responsive layout using Bootstrap 5

---

## 🛠️ Tech Stack

- Python 3.13
- Django 5.2
- Bootstrap 5 (via CDN)
- SQLite (default)
- `widget_tweaks` for form rendering

---

## 📦 Installation

### ✅ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
## 📦 Install dependencies
``` bash
pip install -r requirements.txt
```

🔧 Run migrations
``` bash
python manage.py migrate
```
## 👤 Create a superuser
``` bash
python manage.py createsuperuser
```
##  🚀 Start the development server
``` bash
python manage.py runserver
```
## 🌐 Visit the app

http://127.0.0.1:8000

🔐 Authentication

    All manga management features require login.

    Public pages (like list/detail) can be made accessible without login, depending on project settings.