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
            fields = ('id', 'title', 'poster_path',)
    
    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('pk', 'nickname', 'profile_img')
    
    class CommentSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Comment
            fields = '__all__'
    
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    like_users_cnt = serializers.IntegerField(source='like_users.count', read_only=True)
    movies = MovieSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields= ('pk', 'title', 'movies', 'like_users_cnt','description', 'user', 'like_users', 'comments',)

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
            modle = Movie
            fields = ('pk', 'title', 'poster_path',)
    
    user = UserSerializer(read_only=True)
    movies = MovieSerializer(many=True, read_only=True)
    likes_count =serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Collection
        fields = ('pk', 'title', 'user', 'movies', 'likes_count')

class UserLikesColletctionSerializer(serializers.ModelSerializer):
    pass