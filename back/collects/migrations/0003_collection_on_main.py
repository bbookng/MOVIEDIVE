# Generated by Django 3.2.13 on 2022-11-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collects', '0002_remove_collection_on_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='on_main',
            field=models.BooleanField(default=False),
        ),
    ]