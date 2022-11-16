from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def review_list(request):
    pass

@api_view(['POST'])
def create_review(request, movie_pk):
    pass

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    pass

@api_view(['POST'])
def like_review(request, review_pk):
    pass

@api_view(['GET', 'POST'])
def comments_list(request, review_pk):
    pass

@api_view(['PUT', 'DELETE'])
def comment_status(request, review_pk, comment_pk):
    pass