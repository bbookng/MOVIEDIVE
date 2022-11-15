from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
# 현재 유저의 프로필 정보를 가져옴
@api_view(['GET', 'PUT'])
def get_current_user_profile(request):
    pass

# 특정 사용자의 프로필 정보를 가져옴
@api_view(['GET'])
def get_profile(request, username):
    pass

@api_view(['POST'])
def follow(request, user_pk):
    pass

@api_view(['GET'])
def get_wishlists(request, username):
    pass

@api_view(['GET'])
def get_user_reviews(request, username):
    pass

@api_view(['GET'])
def get_user_collections(request, username):
    pass