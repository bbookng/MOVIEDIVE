from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from .serializers import CollectionCreateSerializer, CollectionUpdateSerializer, CollectionDetailSerializer, CollectionListSerializer, CollectionCommentSerializer, CommentSerializer, AutoCompleteSerializer
from .models import Collection, Comment
from movies.models import Movie
from django.core.paginator import Paginator

# Create your views here.

@api_view(['GET'])
def collections_list(request):
    collections = get_list_or_404(Collection)
    paginator = Paginator(collections, 20)
    page_number = request.GET.get('page')
    current_page = int(page_number) if page_number else 1

    collection_list = paginator.get_page(current_page)
    serializer = CollectionListSerializer(collection_list, many=True)
    return Response(serializer.data)


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
    
@api_view(['POST'])
def comment_create(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    serializer = CollectionCommentSerializer(data=request.data)
    if serializer.is_valid():
        comment = serializer.save(user=request.user, collection = collection)
        serializer = CollectionCommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def comment_status(request, collection_pk, comment_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    def update_comment():
        if comment.user.pk == request.user.pk:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(collection=collection, user=request.user)
                return Response(serializer.data)

    def delete_comment():
        comment.delete()
        serializer = CollectionDetailSerializer(collection)
        return Response(serializer.data)

    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()

@api_view(['GET'])
def get_suggestions(request, keyword):
    movies = Movie.objects.filter(title__contains=keyword).order_by('-vote_average')[:20]
    serializer = AutoCompleteSerializer(movies, many=True)
    return Response(serializer.data)