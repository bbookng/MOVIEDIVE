from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import UpdateUserRequestSerializer, UserNicknameSerializer, UserMessageSerializer, UserLikeMovieSerializer, UserMakesCollectionSerializer, UserReviewSerializer, ProfileResponseSerializer ,PhotoSerializer, UserProfileImageUpdateSerializer


# Create your views here.
# 현재 유저의 프로필 정보를 가져옴

User = get_user_model()

@api_view(['GET'])
def get_current_user_profile(request):
    user = request.user
    serializer = ProfileResponseSerializer(user)   
    return Response(serializer.data)
    
    
@api_view(['PUT'])
def update_profile(request):
    print(1)
    user = request.user
    print(request.data)
    serializer = UpdateUserRequestSerializer(instance=user, data=request.data)
    print(serializer.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# # 특정 사용자의 프로필 정보를 가져옴
# @api_view(['GET'])
# def get_profile(request, username):
#     user = get_object_or_404(get_user_model(), username=username)
#     serializer = ProfileResponseSerializer(user)
#     return Response(serializer.data)

@api_view(['GET', 'PUT'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method=="GET":
        serializer = ProfileResponseSerializer(user)
        return Response(serializer.data)
    elif request.method=="PUT":
        if request.user == user:
            print(1)
            serializer = UpdateUserRequestSerializer(instance=user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # serializer = UpdateUserRequestSerializer(user)
                return Response(serializer.data)
    

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
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserLikeMovieSerializer(user)
    return Response(serializer.data)
    

@api_view(['GET'])
def get_user_reviews(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserReviewSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_collections(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserMakesCollectionSerializer(user)
    return Response(serializer.data)

@api_view(['PUT'])
def set_nickname(request):
    user = request.user
    print(user)
    print(request)
    print(request.data)
    serializer = UserNicknameSerializer(user, request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)

@api_view(['PUT'])
def set_message(request):
    user = request.user
    print(user)

    serializer = UserMessageSerializer(user, request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_profileimg(request):
    profile_img = request.FILES['profile_img']
    data = {
        'profile_img': profile_img
    }
    serializers = PhotoSerializer(data = data)
    if serializers.is_valid():
        serializers.save()
        new_data = { "profile_img": serializers.data['profile_img'] }
        print("new_data", new_data)
        user_serializer = UserProfileImageUpdateSerializer(instance=request.user, data=new_data)
        print(user_serializer)
        if user_serializer.is_valid():
            print(user_serializer.errors)
            user_serializer.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
    print(serializers.errors)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

def change_password(request,):
    if request.method == 'PUT':
        serializer = ChangePasswordSerializer(request.user)
        return Response(serializer.data, safe=False)