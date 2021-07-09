from django.urls import path
from apps.cart import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart_page'),
    path('update/', views.cart_update, name='update_cart'),
]
