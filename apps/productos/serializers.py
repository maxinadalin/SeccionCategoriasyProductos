from rest_framework import serializers
from .models import productos

class ProductosSerializers(serializers.ModelSerializer):
    class Meta:
        model = productos
        field = [
            'id',
            'name',
            'photo',
            'description',
            'price',
            'category',
            'quantity',
            'sold',
            'date_created',
            'price_discount',
            'get_thumbnail',
            'final_price'  
        ]
