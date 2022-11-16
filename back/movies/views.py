from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie
from rest_framework import status
from rest_framework.response import Response
from .serializers import MovieListSerializer, MovieSerializer
from django.db.models import Count

# Create your views here.

@api_view(['GET'])
def movie_list(request):
    keyword = request.GET.get('keyword')

    if keyword:
        movies = Movie.objects.filter(title__contains=keyword).annotate(review_count=Count('reviews', distinct=True), 
        wish_count=Count('wish_users', distinct=True)).order_by('-popularity')
    else:
        movies = Movie.objects.annotate(review_count=Count('reviews', distinct=True), 
        wish_count=Count('wish_users', distinct=True)).order_by('-popularity')

    serializer = MovieListSerializer(movie_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

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