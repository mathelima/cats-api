import django
from django.shortcuts import render
from django import views
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Breeds, Categories
from .serializers import BreedsSerializer, CategoriesSerializer


class BreedsViewSet(viewsets.ModelViewSet):
    queryset = Breeds.objects.all()
    serializer_class = BreedsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ("origin", "temperament")
    search_fields = ['origin', 'temperament']


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
