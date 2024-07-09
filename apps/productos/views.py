from django.shortcuts import render
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.productos.serializers import ProductosSerializers 
from apps.categorias.models import Categoria
from django.db.models import Q
from .models import productos

# Create your views here.

class ProductosView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, productId, format = None ):
        try:
         product_id = int(productId)
        except: 
          return Response ({"message":"error el id del producto debe ser un entero"}, status = status.HTTP_404_NOT_FOUND)
     
        if productos.objects.filter(id=product_id).exists():
          producto = productos.objects.get(id=product_id)
          
          producto = ProductosSerializers(producto)
          
          return Response ({"prodcuto": producto.data}, status = status.HTTP_200_OK)
        else:
            return Response({"message":"no se ha encontrado un producto"},status = status.HTTP_400_BAD_REQUEST )
    

class ListProductView(APIView):

    def get(self, request, format = None):
        if productos.objects.all().exists():
            product = productos.objects.all()
            product = ProductosSerializers(product,many=True)
            return Response ({"Productos":product.data},status =status.HTTP_200_OK)
        else:
            return Response({"message":"no se ha encontrado ningun producto"},status=status.HTTP_400_BAD_REQUEST)


class SearchView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data
        
        search = data["search"]
        
        if search == 0:
            search_result = producto.objects.all()
        else:
            search_result = productos.objects.filter(
                Q(description__icontains=search) | Q(name__icontains=search)
            )

        search_result = ProductosSerializers(search_result, many=True)
        return Response ({"search_result":search_result.data},status= status.HTTP_200_OK)
    
    
class SearchOrderView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self,request,format=None):
        data = self.request.data
        
        try:
            categoria = int(data["categoria_id"])
        except:
            return Response ({"message":"debe ingresar un numero entero"},status=status.HTTP_404_NOT_FOUND)
        
        if categoria == 0 :
            productos_filtrados = productos.objects.filter(categoria=categoria)
        elif not Categoria.objects.filter(id=categoria).exists():
                return Response({"message":"no se encontraron categorias con este id"},status = status.HTTP_404_NOT_FOUND)
        else:
            categoria = Categoria.objects.get(id=categoria)
            if categoria.parent:
                productos_filtrados = productos.objects.filter(categoria=categoria)
            elif not Categoria.objects.filter(parent=categoria).exists():
                productos_filtrados = productos.objects.filter(categoria=categoria)
            else:
                categorias = Categoria.objects.filter(parent=categoria)
                categorias_filtradas = [categoria]
                
                for cat in categorias:
                    categorias_filtradas.append(cat)

                categorias_filtradas = tuple(categorias_filtradas)
                
                productos_filtrados = productos.objects.filter(categoria__in=categorias_filtradas)
        
        productos_filtrados = ProductosSerializers(productos_filtrados,many=True)
        print(productos_filtrados.data)
        if len(productos_filtrados.data) > 0:
            return Response ({"productos_filtrados":productos_filtrados.data}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'No products found'},
                status=status.HTTP_200_OK)