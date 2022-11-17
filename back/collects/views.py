from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from .serializers import CollectionCreateSerializer, CollectionUpdateSerializer, CollectionDetailSerializer
from .models import Collection, Comment
from movies.models import Movie

# Create your views here.

@api_view(['GET'])
def collections_list(request):
    pass

@api_view(['POST'])
def create_collection(request):
    serializer = CollectionCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)

    def collection_detail():
        serializer = CollectionDetailSerializer(collection)
        return Response(serializer.data)

    def update_collection():
        serializer = CollectionUpdateSerializer(instance=collection, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)

    def delete_collection():
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return collection_detail()
    elif request.method == 'PUT':
        if request.user == collection.user:
            return update_collection()
    elif request.method == 'DELETE':
        if request.user == collection.user:
            return delete_collection()

@api_view(['POST'])
def like_collection(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    user = request.user

    if collection.like_users.filter(pk=user.pk).exists():
        collection.like_users.remove(user)
        serializer = CollectionDetailSerializer(collection)
        return Response(serializer.data)
    else:
        collection.like_users.add(user)
        serializer = CollectionDetailSerializer(collection)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def comments_list(request, collection_pk):
    comments = get_list_or_404(Comment, pk=collection_pk)

@api_view(['PUT', 'DELETE'])
def comment_status(request, collection_pk):
    pass