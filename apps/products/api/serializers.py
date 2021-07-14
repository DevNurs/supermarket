from rest_framework import serializers
from apps.products.models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
