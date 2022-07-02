from django.shortcuts import render
from rest_framework import viewsets
from .models import Links
from rest_framework.generics import ListAPIView 
from rest_framework.generics import CreateAPIView 
from rest_framework.generics import RetrieveAPIView 
from rest_framework.generics import UpdateAPIView 
from rest_framework.generics import DestroyAPIView

from .serializers import LinkSerializer
# Create your views here.

class PostListApi(ListAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(CreateAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi(RetrieveAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(UpdateAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(DestroyAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer