from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product
# for fun base viwe
from django.http import HttpRequest, JsonResponse, HttpResponse
# for drf
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
# for API view
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
# authentication, permission
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
# for users
from django.contrib.auth import get_user_model
#class base swagger
from drf_spectacular.utils import extend_schema

User = get_user_model()


# region view
# class Home(TemplateView):
#     context ={
#         'products': Product.objects.all()
#     }
#     template_name = "home/home.html"

# endregion

# region function view 
# api view
# @api_view(['GET'])
# def product_json(request: Request):
#     products = list(Product.objects.all().values())
#     return Response({'products': products}, status.HTTP_200_OK)

# endregion

#region function base view

@api_view(['GET', 'POST'])
def all_product(request:Request):
    if request.method == 'GET':
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        return Response(product_serializer.data, status.HTTP_200_OK)
    elif request.method =='POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)  
    return Response(None,status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def product_detail_view(requst: Request, product_id:int):
        try:
             product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
             return Response(None, status.HTTP_404_NOT_FOUND)
        if requst.method == 'GET':
             serializer = ProductSerializer(product)
             return Response(serializer.data, status.HTTP_200_OK)
        elif requst.method == 'PUT':
             serializer = ProductSerializer(product, data=requst.data)
             if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status.HTTP_202_ACCEPTED)
             return Response(None, status.HTTP_400_BAD_REQUEST)
             
        elif requst.method == 'DELETE':
             product.delete()
             return Response(None,status.HTTP_204_NO_CONTENT)

# endregion
             

#region class base view

class ManageProductApiView(APIView):
     # swagger view
     @extend_schema(
        request=ProductSerializer,
        responses={201: ProductSerializer},
        description='this api is used for get all product list'
    )
     def get(self,request:Request):
         products = Product.objects.all()
         product_serializer = ProductSerializer(products, many=True)
         return Response(product_serializer.data, status.HTTP_200_OK)
     
     def post(self,request:Request):
         serializer = ProductSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)  
     #     return Response(None,status.HTTP_400_BAD_REQUEST)
     


class ProductDetailApiView(APIView):
     def get_object(self,pk:int):
         try:
             product = Product.objects.get(pk=pk)
             return product
         except Product.DoesNotExist:
             return Response(None, status.HTTP_404_NOT_FOUND)
     def get(self,request: Request,pk):
          Product = self.get_object(pk)
          serializer = ProductSerializer(Product)
          return Response(serializer.data, status.HTTP_200_OK)
          
     def put(self,request: Request,pk):
          Product = self.get_object(pk)
          serializer = ProductSerializer(Product, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status.HTTP_202_ACCEPTED)
          return Response(None, status.HTTP_400_BAD_REQUEST)
          
     def delete(self,request: Request,pk):
          Product = self.get_object(pk)
          Product.delete()
          return Response(None,status.HTTP_204_NO_CONTENT)
     

#endregion
    

# region mixins

class ProductListMixinApiView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer

     def get(self,request:Request):
          return self.list(request)
     
     def post(self,request:Request):
          return self.create(request)
     
class ProductDetailtMixinApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer

     def get(self,request:Request,pk):
          return self.retrieve(request,pk)
     
     def put(self,request:Request,pk):
          return self.update(request,pk)
     
     def delete(self,request:Request,pk):
          return self.destroy(request,pk)

# endregion


# region generics

class ProductGenericApiViewPagination(PageNumberPagination):
     page_size = 3

class ProductGenericApiView(generics.ListCreateAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     pagination_class = ProductGenericApiViewPagination
     # authentication_classes = [BasicAuthentication]
     # permission_classes = [IsAuthenticated]


class ProductGenericDetailApiView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
# endregion

# region viewsets

class ProductViewSetApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination

# endregion

# # region user

# class UserGenericApiView(generics.ListCreateAPIView):
#      queryset = User.objects.all()
#      serializer_class = UserSerializer

# # endregion
