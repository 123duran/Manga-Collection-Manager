# mangas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.manga_list, name='manga_list'),  # List all mangas
    path('<int:manga_id>/', views.manga_detail, name='manga_detail'),  # Manga Details
    path('chapter/<int:id>/toggle-owned/', views.toggle_owned_chapter, name='toggle_owned_chapter'),  # Toggle ownership
    path('manga/<int:manga_id>/create-chapter/', views.create_chapter, name='create_chapter'),  # Create chapter
]