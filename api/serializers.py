from rest_framework import serializers
from .models import *


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['id', 'title', 'description',
                  'images', 'parent', 'created_at']


class SubCategorySerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'parent', 'created_at',  'products']


class CategoriesSerializer(serializers.ModelSerializer):
    data = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ['id', 'name', 'created_at', 'parent', 'data']
