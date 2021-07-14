from rest_framework import generics
from apps.products.api import serializers
from apps.products.models import Product, ProductImage


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductImageCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
