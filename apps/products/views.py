from apps.products.models import Product, ProductImage
from apps.products.forms import ProductForm, ProductImageForm
from django.forms import inlineformset_factory
from django.views.generic import ListView, DetailView
from django.db.models import Q

from django.shortcuts import render, redirect, get_object_or_404


class ProductIndexView(ListView):
    queryset = Product.objects.all()[:8]
    model = Product
    template_name = 'products/index_cbv.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'


class ProductSlugView(DetailView):
    model = Product
    template_name = 'products/detail.html'


class ProductGalleryView(ListView):
    model = Product
    paginate_by = 4
    template_name = 'products/index_gallery.html'
    context_object_name = 'products'


class ProductSearchView(ListView):
    model = Product
    paginate_by = 4
    template_name = 'products/index_gallery.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()
        qury_obj = self.request.GET.get('key')
        if qury_obj:
            queryset = Product.objects.filter(
                Q(title__icontains=qury_obj)
            )
        return queryset


def index(request):
    product = Product.objects.all()
    return render(request, 'products/index.html', {'products': product})


def detail(request, id):
    product = get_object_or_404(Product, id=id)
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
