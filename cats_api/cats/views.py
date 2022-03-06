import django
from django.shortcuts import render
from django import views
from rest_framework import viewsets
from .models import Breeds, Categories
from .serializers import BreedsSerializer, CategoriesSerializer


class BreedsViewSet(viewsets.ModelViewSet):
    queryset = Breeds.objects.all()
    serializer_class = BreedsSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
