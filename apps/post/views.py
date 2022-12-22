from django.shortcuts import render

from apps.post.models import Post
from apps.post.serialazers import Postserializer, PostCreateSerializer
from rest_framework import generics

# Create your views here.

class PostAPIView(generics.ListAPIView):
    queryset =  Post.objects.all()
    serializer_class = Postserializer

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    