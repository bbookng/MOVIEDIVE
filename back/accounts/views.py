from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import CurrentUserResponseSerializer, UpdateUserRequestSerializer


# Create your views here.
# 현재 유저의 프로필 정보를 가져옴

User = get_user_model()

@api_view(['GET'])
def get_current_user_profile(request):
    user = request.user
    serializer = CurrentUserResponseSerializer(user)   
    return Response(serializer.data)
    
    

@api_view(['PUT'])
def update_profile(request):
    user = request.user
    serializer = UpdateUserRequestSerializer(instance=user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    
    

# 특정 사용자의 프로필 정보를 가져옴
@api_view(['GET'])
def get_profile(request, username):
    user = get_object_or_404(User, username)
    

@api_view(['POST'])
def follow(request, user_pk):
    user = get_object_or_404(get_user_model(), pk = user_pk)
    if user != request.user:
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
        return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def get_likelists(request, username):
    user = get_object_or_404(get_user_model(), username)
    pass
    

@api_view(['GET'])
def get_user_reviews(request, username):
    pass

@api_view(['GET'])
def get_user_collections(request, username):
    pass