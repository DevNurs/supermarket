from django.urls import path
from apps.products.views import ProductIndexView, create_product, detail

urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
    path('create/', create_product, name='create'),
    path('detail/<int:id>/', detail, name='detail'),
]
