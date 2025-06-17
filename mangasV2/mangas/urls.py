# mangas/urls.py

from django.urls import path
from . import views
from .views import MangaDeleteView, MangaUpdateView

urlpatterns = [
    path('', views.manga_list, name='manga_list'),  # List all mangas
    path('<int:manga_id>/', views.manga_detail, name='manga_detail'),  # Manga Details
    path('chapter/<int:id>/toggle-owned/', views.toggle_owned_chapter, name='toggle_owned_chapter'),  # Toggle ownership
    path('manga/<int:manga_id>/create-chapter/', views.create_chapter, name='create_chapter'),  # Create chapter
    path('create/', views.manga_create, name='manga_create'), # Create Manga
    path('manga/<int:pk>/delete/', MangaDeleteView.as_view(), name='manga_delete'), #delete manga
    path('manga/<int:pk>/edit/', MangaUpdateView.as_view(), name='manga_edit'),
]