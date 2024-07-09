from django.urls import path
from .views import ProductosView,ListProductView,SearchView,SearchOrderView

urlpatterns = [
    path("detallePorducto/<productId>",ProductosView.as_view()),
    path("Productos",ListProductView.as_view()),
    path("search",SearchView.as_view()),
    path("search/by",SearchOrderView.as_view())
]

