# 3.1
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('api/categorias/',include("apps.categorias.urls")),
    path('api/productos/',include("apps.productos.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #we add static to work 

urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]
