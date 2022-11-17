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
        

# 보류
class ProfileResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'profile_img', 'message',)

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
