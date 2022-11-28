from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Image
from movies.models import Movie
from collects.models import Collection
from community.models import Review

class UpdateUserRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'message',)
        
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
        
        class CollectionMovieSerializer(serializers.ModelSerializer):
            
            class Meta:
                model = Movie
                fields = ('pk', 'title', 'poster_path')
        
        movies = CollectionMovieSerializer(many=True, read_only=True)
        
        class CollectionUserSerializer(serializers.ModelSerializer):
            
            class Meta:
                model = get_user_model()
                fields = ('pk', 'id', 'username', 'nickname')
        
        user = CollectionUserSerializer(read_only=True)
        like_users_cnt = serializers.IntegerField(source='like_users.count', read_only=True)
        comments_cnt = serializers.IntegerField(source='collection_comments.count', read_only=True)

        
        class Meta:
            model = Collection
            fields = ('pk', 'title', 'movies', 'like_users', 'user', 'like_users_cnt', 'comments_cnt')
    
    collections = MadeCollectionSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        fields = ('collections', 'username', 'nickname', 'id', 'pk',)
        
class UserReviewSerializer(serializers.ModelSerializer):
      
    class ReviewSerializer(serializers.ModelSerializer):
        
        class ReviewMovieSerializer(serializers.ModelSerializer):
            
            class Meta:       
                model = Movie
                fields = ('pk', 'id', 'title',)
            
        movie = ReviewMovieSerializer(read_only=True)
        
        class Meta:
            model = Review
            fields = ('id', 'pk', 'title', 'user', 'movie', 'content')
        
    
    reviews = ReviewSerializer(many=True, read_only=True)
    
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

# 리뷰 갯수, 팔로잉, 팔로워, 내가 만든 컬렉션 추가
class ProfileResponseSerializer(serializers.ModelSerializer):
    followers_cnt = serializers.IntegerField(source='followers.count', read_only=True)
    followings_cnt = serializers.IntegerField(source='followings.count', read_only=True)
    reviews_cnt = serializers.IntegerField(source='reviews.count', read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'pk', 'username', 'nickname', 'profile_img', 'message', 'followings_cnt', 'reviews', 'reviews_cnt', 'followers_cnt', 'created_string',)
        
        
# class CurrentUserResponseSerializer(serializers.ModelSerializer):
#     # reviews = UserReviewSerializer(many=True, read_only=True)
#     followings_cnt = serializers.IntegerField(source='followings.count', read_only=True)
#     followers_cnt = serializers.IntegerField(source='followers.count', read_only=True)
#     # reviews_cnt = serializers.IntegerField(source='reviews.count', read_only=True)
    
#     class Meta:
#         model = get_user_model()
#         fields = ('id', 'username', 'nickname', 'profile_img', 'message', 'followings_cnt', 'followers_cnt',)
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('__all__')
    
class UserProfileImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('profile_img',)
