from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Collection
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
    
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    like_users_cnt = serializers.IntegerField(source='like_users.count', read_only=True)
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields= ('pk', 'title', 'movies', 'like_users_cnt','description', 'user', 'like_users',)
