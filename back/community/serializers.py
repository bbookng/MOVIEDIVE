from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Review, Comment


class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = ('movie', 'movie_title', 'id', 'title', 'content', 'user', 'username', 'created_string',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)


class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = ('title', 'content', 'created_at', 'id', 'like_users', 'movie', 'movie_title', 'rate', 'updated_at', 'user', 'username', 'comment_set', 'comment_count', 'created_string',)
        read_only_fields = ('user', )