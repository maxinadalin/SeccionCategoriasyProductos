from django.urls import path
from .views import ProductosView

urlpatterns = [
    path("detallePorducto",ProductosView.as_view())
]
