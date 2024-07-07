from .views import CategoriaView
from django.urls import path

urlpatterns = [
    path("categorias",CategoriaView.as_view()),
]
