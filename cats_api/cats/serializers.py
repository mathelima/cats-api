from rest_framework import serializers
from .models import Breeds, Categories


class BreedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breeds
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
