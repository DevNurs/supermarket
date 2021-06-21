from django.urls import path
from apps.products import views

urlpatterns = [
    path('', views.ProductIndexView.as_view(), name='index'),
    path('create/', views.create_product, name='create'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail_pk'),
    path('<str:slug>/', views.ProductSlugView.as_view(), name='detail')
]
