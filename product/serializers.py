from rest_framework import serializers
from .models import ProductInfo, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductInfo
        fields=['id','name', 'description','price',  'pr_date', 'brand']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']