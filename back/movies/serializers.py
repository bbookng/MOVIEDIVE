from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ('pk', 'name',)
        
        
class MovieListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    like_users = UserSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'poster_path', 'vote_average', 'like_users', 'genres')
        

class MovieSerializer(serializers.ModelSerializer):
    pass