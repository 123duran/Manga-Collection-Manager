from django.db import models

# Create your models here.
from django.db import models

class Manga(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")  # Title of the manga
    author = models.CharField(max_length=100, verbose_name="Author")  # Author of the manga
    volumes = models.PositiveIntegerField(verbose_name="Number of Volumes", default=1)  # Number of volumes
    release_date = models.DateField(verbose_name="Release Date", null=True, blank=True)  # Release date (optional)
    description = models.TextField(verbose_name="Description", blank=True, null=True)  # Description or synopsis (optional)
    cover = models.CharField(max_length=350, verbose_name="Cover", blank=True, null=True)  # Cover URL or text (optional)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Date Added")  # Date and time when the manga was added

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Manga"
        verbose_name_plural = "Mangas"

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='chapters', verbose_name="Manga")  # FK for manga
    number = models.PositiveIntegerField(verbose_name="Chapter Number")  # Chapter number
    date_acquired = models.DateField(verbose_name="Date Acquired", null=True, blank=True)  # Acquisition date (optional)
    owned = models.BooleanField(default=False, verbose_name="Owned")  # Owned or not

    def __str__(self):
        return f"{self.manga.title} - Chapter {self.number}"

    class Meta:
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"