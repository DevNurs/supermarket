from django.urls import path
from apps.users.api import views

urlpatterns = [
    path('', views.UserAPIView.as_view(), name='user-api'),
    path('current-user/', views.current_user, name='current-user'),
]
