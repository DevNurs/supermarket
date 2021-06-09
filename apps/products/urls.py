from django.urls import path
from apps.products.views import index, create_product, detail

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_product, name='create'),
    path('detail<int:id>/', detail, name='detail'),
]
