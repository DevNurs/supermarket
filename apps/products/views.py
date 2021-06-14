from apps.products.models import Product, ProductImage
from apps.products.forms import ProductForm, ProductImageForm
from django.forms import inlineformset_factory

from django.shortcuts import render, redirect


def index(request):
    product = Product.objects.all()
    return render(request, 'products/index.html', {'products': product})


def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/detail.html', {'product': product})


def create_product(request):
    form = ProductForm(request.POST, None)
    ProductImageFormset = inlineformset_factory(Product, ProductImage, form=ProductImageForm, extra=1)
    if form.is_valid():
        product = form.save()
        formset = ProductImageFormset(request.POST, request.FILES, instance=product)
        if formset.is_valid():
            formset.save()
        return redirect('index')
    formset = ProductImageFormset()
    return render(request, 'products/create.html', locals())
