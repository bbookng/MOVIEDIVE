# Generated by Django 3.2.13 on 2022-11-16 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_collections', to=settings.AUTH_USER_MODEL)),
                ('movies', models.ManyToManyField(related_name='collections', to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]