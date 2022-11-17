from django.contrib import admin
from .models import Review, Comment


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('movie',)

admin.site.register(Review)
admin.site.register(Comment)