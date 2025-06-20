# Generated by Django 5.2.3 on 2025-06-06 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('author', models.CharField(max_length=100, verbose_name='Author')),
                ('volumes', models.PositiveIntegerField(default=1, verbose_name='Number of Volumes')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release Date')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('cover', models.CharField(blank=True, max_length=350, null=True, verbose_name='Cover')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
            ],
            options={
                'verbose_name': 'Manga',
                'verbose_name_plural': 'Mangas',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Chapter Number')),
                ('date_acquired', models.DateField(blank=True, null=True, verbose_name='Date Acquired')),
                ('owned', models.BooleanField(default=False, verbose_name='Owned')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='mangas.manga', verbose_name='Manga')),
            ],
            options={
                'verbose_name': 'Chapter',
                'verbose_name_plural': 'Chapters',
            },
        ),
    ]
