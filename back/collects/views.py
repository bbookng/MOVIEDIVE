from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def collections_list(request):
    pass

@api_view(['POST'])
def create_collection(request):
    pass

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def collection_detail(request, collection_pk):
    pass

@api_view(['POST'])
def like_collection(request, collection_pk):
    pass

@api_view(['GET', 'POST'])
def comments_list(request, collection_pk):
    pass

@api_view(['PUT', 'DELETE'])
def comment_status(request, collection_pk):
    pass