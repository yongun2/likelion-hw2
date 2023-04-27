from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from ch13.DjangoApi.products.models import Product
from ch13.DjangoApi.products.serializers import ProductSerializer

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
