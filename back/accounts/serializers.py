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
        fields = ('nickname', 'profile_img')
        

# 보류
class ProfileResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('nickname', 'profile_img')
        
