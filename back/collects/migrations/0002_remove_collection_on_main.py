# Generated by Django 3.2.13 on 2022-11-19 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='on_main',
        ),
    ]
