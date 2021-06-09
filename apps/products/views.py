from apps.products.models import Product
from apps.products.forms import ProductForm

from django.shortcuts import render, redirect


def index(request):
    product = Product.objects.all()
    return render(request, 'products/index.html', {'products': product})


def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/detail.html', {'product': product})


def create_product(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'products/create.html', {'form': form})
