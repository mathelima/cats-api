from django.contrib import admin
from django.urls import path, include
from .views import BreedsViewSet, CategoriesViewSet
from rest_framework import routers

app_name = "cats"

router = routers.DefaultRouter()
router.register('breeds', BreedsViewSet, basename='Breeds')
router.register('categories', CategoriesViewSet, basename='Categories')

urlpatterns = router.urls
