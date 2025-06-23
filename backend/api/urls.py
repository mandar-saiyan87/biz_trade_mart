from django.urls import path
from .views import ProductList, ProductDetails

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('product/<str:name>/', ProductDetails.as_view())
]