from django.urls import path
from apps.products import views

urlpatterns = [
    path('', views.ProductIndexView.as_view(), name='index'),
    path('create/', views.create_product, name='create'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail_pk'),
    path('detail/<str:slug>/', views.ProductSlugView.as_view(), name='detail'),
    path('gallery/', views.ProductGalleryView.as_view(), name='gallery'),
    path('search/', views.ProductSearchView.as_view(), name='search'),
    path('update/<int:id>/', views.update_product, name='update')
]
