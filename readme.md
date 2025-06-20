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

## 🔧 Run migrations
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
## 🚢 Deployment

This project is configured to automatically deploy to Fly.io using GitHub Actions whenever changes are pushed to the `main` branch.

The workflow defined in `.github/workflows/deploy.yml`:

- Checks out the code
- Sets up Python environment
- Installs dependencies
- Deploys the app to Fly.io using the Fly CLI and a stored `FLY_API_TOKEN` secret

Make sure your Fly.io app is properly configured with a `fly.toml` file in the `mangasV2` directory and that the `FLY_API_TOKEN` secret is added to your GitHub repository settings.

### 🔐 Setting up FLY_API_TOKEN for GitHub Actions

To allow GitHub Actions to deploy to Fly.io, you need to create an access token (`FLY_API_TOKEN`) and add it as a secret in your GitHub repository.

---

#### 1. Create the Fly.io token via terminal (bash)

Run the following command in your terminal to create a deploy token:

```bash
fly tokens create deploy --name "GitHub Actions Token"
```
This will return a token string like:
```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```
Important: Copy this token immediately as you won’t be able to see it again.

#### 2. Add the token as a secret in GitHub

    1. Go to your GitHub repository.

    2. Navigate to 'Settings' > 'Secrets and variables' > 'Actions'.

    3. Click on 'New repository secret'.

    4. Name the secret `FLY_API_TOKEN`.

    5. Paste the token you generated from Fly.io into the value field.

    6. Save the secret.

## 🌐 Visit the app

[https://django-mangas.fly.dev/](https://django-mangas.fly.dev/)

🔐 Authentication

    All manga management features require login.
    Public pages (like list/detail) can be made accessible without login, depending on project settings.