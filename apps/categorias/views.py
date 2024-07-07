from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Categoria
from apps.categorias.serializers import CategoriaSerializers

# Create your views here.


class CategoriaView(APIView):
    def get(self,request,format=None):
        
        if Categoria.objects.all().exists():
            categorias = Categoria.objects.all()
            
            result = []
            
            for categoria in categorias:
                if not categoria.parent:
                    items = {}
                    items["id"] = categoria.id
                    items["name"]=categoria.name
                    items["photo"]=categoria.photo.url if categoria.photo  else None
                    
                    items["sub_categirias"] = []
                    
                    for sub_category in categorias:
                        sub_items={}
                        if sub_category.parent and sub_category.parent.id == categoria.id:
                            sub_items["id"] = sub_category.id
                            sub_items["name"] = sub_category.name
                            sub_items['photo'] = sub_category.photo.url if sub_category.photo else None
                            sub_items['sub_categirias'] = []
                            items["sub_categirias"].append(sub_items)
                    result.append(items)
            
            return Response ({"categorias": result},status = status.HTTP_200_OK)
                    
            
        else:
            return Response({"message":"no se encontraron categorias"},status=status.HTTP_404_NOT_FOUND)
        
        
    