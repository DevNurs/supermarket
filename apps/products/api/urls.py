from django.urls import path
from apps.products.api import views

urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name='product_list_api'),
    path('create/', views.ProductCreateAPIView.as_view(), name='product_create_api'),
    path('image/', views.ProductImageCreateAPIView.as_view(), name='product_image_create_api')
]
