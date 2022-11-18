from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from collects.models import Collection
from community.models import Review

class CurrentUserResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = "__all__"
        

class UpdateUserRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'profile_img', 'message',)
        

# 리뷰 갯수, 팔로잉, 팔로워, 내가 만든 컬렉션 추가
class ProfileResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'profile_img', 'message',)
        
class UserLikeMovieSerializer(serializers.ModelSerializer):
    
    class LikeMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path')
            
    like_movies = LikeMovieSerializer(many=True)
    like_movies_cnt = serializers.IntegerField(source='like_movies.count', read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('like_movies', 'like_movies_cnt')

class UserMakesCollectionSerializer(serializers.ModelSerializer):
    
    class MadeCollectionSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Collection
            fields = ('pk', 'title', 'movies', 'like_users')
    
    collections = MadeCollectionSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        fields = ('collections',)
        
class UserReviewSerializer(serializers.ModelSerializer):
    
    class ReviewSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Review
            fields = ('pk', 'title', 'user', 'movie')
    
    reviews = ReviewSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        fields = ('reviews', )
        
        

class UserNicknameSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(max_length=10)
    
    class Meta:
        model = get_user_model()
        fields = ('nickname',)
    # def update(self, instance, data):
    #     instance.nickname = data.get("nickname", instance.nickname)
    #     instance.save()
    #     return instance
        
class UserMessageSerializer(serializers.ModelSerializer):
    message = serializers.CharField(max_length=30)
    
    class Meta:
        model = get_user_model()
        fields = ('message',)
        
        