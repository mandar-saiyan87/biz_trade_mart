from threading import get_ident

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetails(APIView):
    def get_object(self, name):
        try:
            get_id = name.split('-')
            product_id = int(get_id[-1])
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, name):
        product = self.get_object(name)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
