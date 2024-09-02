from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from users.models import User
from product.models import ProductInfo, Category
from rest_framework import status
from users.serializers import UserSerializer
from product.serializers import ProductSerializer
from rest_framework.views import APIView
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    # print(request.user.is_authenticated)
    users = User.objects.filter(is_active=True)
    print(users)
    user_serialize = UserSerializer(users,many=True)

    return JsonResponse(content_type='application/json',data=user_serialize.data,status=status.HTTP_200_OK,safe=False)

@api_view(['GET'])
def get_product(request):
    product=ProductInfo.objects.all()
    product_serializer=ProductSerializer(product, many=True)
    print(type(product_serializer.data))
    return JsonResponse(content_type='application/json',data=product_serializer.data,status=status.HTTP_200_OK,safe=False)

@api_view(['GET','POST'])
def func_product(request):
    if request.method == "GET":
        product=ProductInfo.objects.all()
        product_serializer=ProductSerializer(product, many=True)
        print(type(product_serializer.data))
        return JsonResponse(content_type='application/json',data=product_serializer.data,status=status.HTTP_200_OK,safe=False)
    elif request.method == "POST":
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return JsonResponse(content_type='application/json',data={"message":"ok"},status=status.HTTP_200_OK,safe=False)
        else:
            return JsonResponse(content_type='application/json',data={"message":"not ok"},status=status.HTTP_500_INTERNAL_SERVER_ERROR,safe=False)
        
    else:
        return JsonResponse(content_type='application/json',data={"message":"not allow"},status=status.HTTP_400_BAD_REQUEST,safe=False)
    

class ManageProduct(APIView):
    def get(self,request):
        product=ProductInfo.objects.all()
        product_serializer=ProductSerializer(product, many=True)
        print(type(product_serializer.data))
        return JsonResponse(content_type='application/json',data=product_serializer.data,status=status.HTTP_200_OK,safe=False)