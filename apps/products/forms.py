from apps.products.models import Product
from django.forms import ModelForm


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'quantity', 'is_stock']
