from rest_framework import serializers
from .models import Categoria

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields = [
            "parent",
            "name",
            "date_created",
            "photo"
        ]