from rest_framework import generics, viewsets
from apps.categories.api import serializers
from apps.categories.models import Category


class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.filter(parent=None)
    serializer_class = serializers.CategorySerializer

    def get_serializer_class(self):
        if self.action in ['create']:
            return serializers.CategoryCreateSerializer
        return self.serializer_class
