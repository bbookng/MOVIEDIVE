from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from .serializers import CollectionCreateSerializer, CollectionDetailSerializer
from .models import Collection
from movies.models import Movie

# Create your views here.

@api_view(['GET'])
def collections_list(request):
    pass

@api_view(['POST'])
def create_collection(request):
    processed_data = request.data
    
    movies = []
    for movie in request.data['movies']:
        movies.append(movie['pk'])
    
    processed_data['movies'] = movies

    serializer = CollectionCreateSerializer(data=processed_data)

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
        if request.user == collection.user:
            processed_data = request.data
            edited_movies=[]
            print(request.data)
            for movie in request.data['movies']:
                if 'pk' in movie.keys():
                    edited_movies.append(movie['pk'])
                else:
                    edited_movies.append(movie['id'])

            print(processed_data)

            processed_data['movies'] = edited_movies
            serializer = CollectionCreateSerializer(instance=collection, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serializer = CollectionDetailSerializer(collection)
                return Response(serializer.data)

        def delete_collection():
            if request.user == collection.user:
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
    pass

@api_view(['PUT', 'DELETE'])
def comment_status(request, collection_pk):
    pass