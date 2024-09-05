from rest_framework import serializers
from .models import ProductInfo

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductInfo
        fields=['id','name', 'description','price', 'image', 'category']

