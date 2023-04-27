
from rest_framework import serializers

from ch13.DjangoApi.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "product_name", "price")