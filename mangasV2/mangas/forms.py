from django import forms
from django.forms import DateInput
from .models import Manga


class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'author', 'volumes', 'release_date', 'description', 'cover']
        labels = {
            'title': 'Título',
            'author': 'Autor',
            'volumes': 'Número de volumes',
            'release_date': 'Data de lançamento',
            'description': 'Descrição',
            'cover': 'URL da capa',
        }
        widgets = {
            'release_date': DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }