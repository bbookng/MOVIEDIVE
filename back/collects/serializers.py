from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Collection, Comment
from movies.models import Movie

class CollectionCreateSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('id', 'nickname',)
    
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    like_users_cnt = serializers.IntegerField(source='like_users.count', read_only=True)
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model= Collection
        fields= ('pk', 'title', 'movies', 'like_users_cnt', 'description', 'user', 'like_users',)

class CollectionDetailSerializer(serializers.ModelSerializer):
    
    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', 'backdrop_path')
    
    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('pk', 'nickname', 'profile_img')
    
    class CommentSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Comment
            fields = ('pk', 'user', 'content', 'created_at', 'created_string',)
            read_only_fields = ('collection', )
            
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    like_users_cnt = serializers.IntegerField(source='like_users.count', read_only=True)
    movies = MovieSerializer(many=True, read_only=True)
    collection_comments = CommentSerializer(many=True, read_only=True)
    comments_cnt = serializers.IntegerField(source='collection_comments.count', read_only=True)

    class Meta:
        model = Collection
        fields= ('id', 'user', 'title', 'movies', 'description', 'like_users', 'like_users_cnt', 'collection_comments', 'comments_cnt', 'created_at', 'created_string',)

class CollectionUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Collection
        fields= ('title', 'movies', 'description',)
    
class CollectionListSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('pk', 'nickname', 'profile_img')
            
    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_path',)
    
    user = UserSerializer(read_only=True)
    movies = MovieSerializer(many=True, read_only=True)
    likes_count =serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Collection
        fields = ('pk', 'title', 'user', 'movies', 'likes_count')

class CollectionCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('pk', 'content',)

class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('id', 'nickname', 'profile_img')
    
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'created_at', 'created_string')
        read_only_fields = ('collection',)

class AutoCompleteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields= ('pk', 'title', 'poster_path')