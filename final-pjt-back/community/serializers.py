from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Review, Comment
from movies.models import Movie

class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('id', 'nickname', 'profile_img',)
    
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'created_at', 'created_string',)

class ReviewListSerializer(serializers.ModelSerializer):

    class ReviewUserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'nickname', 'profile_img')

    user = ReviewUserSerializer(read_only=True)
    comment_count = serializers.IntegerField(source='community_comments.count', read_only=True)
    like_reviews_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Review
        fields = ('movie', 'movie_title', 'id', 'title', 'content', 'user', 'created_string', 'comment_count', 'like_reviews_count')


class ReviewSerializer(serializers.ModelSerializer):
    
    class ReviewUserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'nickname', 'profile_img')
            
    user = ReviewUserSerializer(read_only=True)
    community_comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='community_comments.count', read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'

class ReviewCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('pk', 'content',)
