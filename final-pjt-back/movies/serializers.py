from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie
from community.models import Review
from collects.models import Collection
        
        
class MovieListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    like_users = UserSerializer(many=True)
    # genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'poster_path', 'backdrop_path', 'vote_average', 'like_users', 'genres')
        

class MovieSerializer(serializers.ModelSerializer):
    
    class MovieReviewSerializer(serializers.ModelSerializer):

        class UserSerializer(serializers.ModelSerializer):

            class Meta:
                model = get_user_model()
                fields = ('pk', 'nickname', 'profile_img')
        
        user = UserSerializer(read_only=True)

        class Meta:
            model = Review
            fields = ('pk', 'user', 'title', 'created_at', 'updated_at', 'created_string')
    
    reviews = MovieReviewSerializer(many=True, read_only=True)
    
    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('pk', 'nickname', 'profile_img',)

    like_users = UserSerializer(many=True, read_only=True)
    like_users_cnt = serializers.IntegerField(source='like_users.count', read_only=True)
    
    class Meta:
        model = Movie
        fields = ('pk', 'like_users_cnt', 'like_users', 'title', 'overview', 'poster_path', 'vote_average', 'reviews', 'backdrop_path', 'genres' ,'wavve','watcha')

class AutoCompleteSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Movie
        fields = '__all__'

        
class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):   
        class Meta:
            model = get_user_model()
            fields = ('pk', 'nickname', 'profile_img')
            
    user = UserSerializer(read_only=True)
    
    class Meta:    
        model = Review
        fields = ('user', 'content', 'title', 'created_at')
        
