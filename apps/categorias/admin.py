from django.contrib import admin
from .models import Categoria
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','parent')
    list_display_links = ('id','name','parent')
    search_fields = ('name', 'parent')
    list_per_page = 25
    
admin.site.register(Categoria, CategoryAdmin)