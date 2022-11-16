from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def movie_list(request):
    pass

@api_view(['GET'])
def movie_detail(request, movie_pk):
    pass

@api_view(['POST'])
def like_movie(request, movie_pk):
    pass


# reviews 와 collections 역참조 하기

@api_view(['GET'])
def movie_reviews(request, movie_pk):
    pass

@api_view(['GET'])
def movie_collections(request, movie_pk):
    pass

@api_view(['GET'])
def auto_complete(request, keyword):
    pass