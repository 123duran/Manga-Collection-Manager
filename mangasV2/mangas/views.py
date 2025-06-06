from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Manga, Chapter

def manga_list(request):
    mangas = Manga.objects.all()  # Retrieve all mangas
    return render(request, 'mangas/manga_list.html', {'mangas': mangas})

def manga_detail(request, manga_id):
    manga = get_object_or_404(Manga, id=manga_id)
    chapters = manga.chapters.all()
    chapter_count = chapters.count()

    owned_count = chapters.filter(owned=True).count()

    owned_percent = round((owned_count / chapter_count) * 100) if chapter_count > 0 else 0

    return render(request, 'mangas/manga_detail.html', {
        'manga': manga,
        'chapter_count': chapter_count,
        'owned_percent': owned_percent,
    })

def toggle_owned_chapter(request, id):
    chapter = get_object_or_404(Chapter, id= id)
    if not chapter.owned:  # Se o capítulo não estava marcado como "possui"
        chapter.owned = True
        chapter.date_acquired = timezone.now().date()  # Define a data atual
    else:  # Se o capítulo estava marcado como "possui"
        chapter.owned = False
        chapter.date_acquired = None  # Remove a data de aquisição
    chapter.save()
    return redirect(reverse('manga_detail', args=[chapter.manga.id]))  # Redireciona de volta para a página do mangá

def create_chapter(request, manga_id):
    manga = get_object_or_404(Manga, id =manga_id)

    last_chapter = Chapter.objects.filter(manga=manga).order_by('-number').first()
    next_number = last_chapter.number + 1 if last_chapter else 1

    Chapter.objects.create(
    manga=manga,
    number=next_number,
    owned=False)
    
    return redirect(reverse('manga_detail', args=[manga.id]))  # Redireciona de volta para a página do mangá