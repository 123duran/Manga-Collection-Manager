#!/bin/bash
set -e

echo "Rodando migrations..."
python manage.py migrate

echo "Criando superusuário se não existir..."
python manage.py shell << END
from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if username and email and password:
    if not User.objects.filter(username=username).exists():
        print(f"Criando superusuário {username}")
        User.objects.create_superuser(username, email, password)
    else:
        print(f"Superusuário {username} já existe")
else:
    print("Variáveis de ambiente do superusuário não definidas, pulando criação")

END

echo "Verificando dados de Manga e Chapter..."

python manage.py shell << END
from mangas.models import Manga, Chapter
if Manga.objects.exists() or Chapter.objects.exists():
    print("Dados de Manga e/ou Chapter já existem, pulando importação.")
else:
    print("Nenhum dado encontrado. Importando mangas_data.json...")
    import os
    os.system('python manage.py loaddata mangas_data.json')
END

echo "Iniciando Gunicorn..."
exec gunicorn mangasV2.wsgi:application --bind 0.0.0.0:8080
