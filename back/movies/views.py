from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie
from rest_framework import status
from rest_framework.response import Response
from .serializers import MovieListSerializer, MovieSerializer, AutoCompleteSerializer, ReviewSerializer
from django.db.models import Count
from django.core.paginator import Paginator
from community.models import Review

# Create your views here.

@api_view(['GET'])
def movie_list(request):
    keyword = request.GET.get('keyword')

    if keyword:
        movies = Movie.objects.filter(title__contains=keyword).annotate(review_count=Count('reviews', distinct=True), 
        like_count=Count('like_users', distinct=True)).order_by('-popularity')
    else:
        movies = Movie.objects.annotate(review_count=Count('reviews', distinct=True), 
        like_count=Count('like_users', distinct=True)).order_by('-popularity')
    
    movies = get_list_or_404(Movie)
    paginator = Paginator(movies, 20)
    page_number = request.GET.get('page')
    current_page = int(page_number) if page_number else 1

    movie_list = paginator.get_page(current_page)
    serializer = MovieListSerializer(movie_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        return Response(status=status.HTTP_200_OK)
    else:
        movie.like_users.add(user)
        return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_reviews(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = Review.objects.filter(movie=movie).annotate(likes_cnt = Count('like_users', distinct=True)).order_by('-like_cnt')[:3]
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def movie_collections(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    pass

@api_view(['GET'])
def auto_complete(request, keyword):
    movies = Movie.objects.filter(title__contains=keyword).order_by('-vote_average')[:10]
    serializer = AutoCompleteSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_new_movies(request):
    movies = Movie.objects.order_by('-release_date')[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

def random_collections():
    pass