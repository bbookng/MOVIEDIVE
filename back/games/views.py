from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def actor_quiz(request):
    pass

@api_view(['GET'])
def ox_quiz(request):
    pass

@api_view(['GET'])
def user_exp(request, user_pk):
    pass