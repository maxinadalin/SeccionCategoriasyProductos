from django.shortcuts import render
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.productos.serializers import ProductosSerializers 
from apps.categorias.models import Categoria
from django.db.models import Q

# Create your views here.

class ProductosView(APIView):
    def get(self, request, product_id, format = None ):
        print("esto funciona")
    
        return Response ({"message":"esto va queriendo loco"},status= status.HTTP_200_OK)