# Generated by Django 3.2.13 on 2022-11-16 05:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('release_date', models.TextField()),
                ('original_title', models.CharField(max_length=100)),
                ('poster_path', models.CharField(max_length=100)),
                ('backdrop_path', models.CharField(max_length=100)),
                ('vote_average', models.FloatField(default=0)),
                ('vote_count', models.IntegerField(default=0)),
                ('popularity', models.FloatField(default=0)),
                ('adult', models.BooleanField(default=False)),
                ('view_cnt', models.IntegerField(default=0)),
                ('genres', models.ManyToManyField(related_name='genre_movies', to='movies.Genre')),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
                ('related_movies', models.ManyToManyField(blank=True, related_name='_movies_movie_related_movies_+', to='movies.Movie')),
            ],
        ),
    ]
