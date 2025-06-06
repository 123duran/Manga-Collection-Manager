from django.contrib import admin

# Register your models here.
from .models import Manga, Chapter

@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'volumes', 'release_date', 'date_added')
    search_fields = ('title', 'author')

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('manga', 'number', 'owned', 'date_acquired')
    list_filter = ('owned', 'manga')