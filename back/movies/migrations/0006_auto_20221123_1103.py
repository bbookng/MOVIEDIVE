# Generated by Django 3.2.13 on 2022-11-23 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20221123_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='adult',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='original_title',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='view_cnt',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='vote_count',
        ),
    ]
