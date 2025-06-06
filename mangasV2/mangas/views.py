from django.shortcuts import render
# mangas/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem-vindo ao app Mangás!")

