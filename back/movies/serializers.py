from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre
from community.models import Review
from collects.models import Collection


# class GenreSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Genre
#         fields = ('pk', 'name',)
        
        
class MovieListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    # like_users = UserSerializer(many=True)
    # genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'backdrop_path', 'vote_average', 'like_users')
        

class MovieSerializer(serializers.ModelSerializer):
    
    class MovieReviewSerializer(serializers.ModelSerializer):

        class UserSerializer(serializers.ModelSerializer):

            class Meta:
                model = get_user_model()
                fields = ('pk', 'nickname')
        
        user = UserSerializer(read_only=True)

        class Meta:
            model = Review
            fields = ('pk', 'user', 'title', 'created_at', 'updated_at')
    
    reviews = MovieReviewSerializer(many=True)
    
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'poster_path', 'vote_average', 'reviews')

class AutoCompleteSerializer(serializers.ModelSerializer):

    class Meta:
        
        model=Movie
        fields=('title',)