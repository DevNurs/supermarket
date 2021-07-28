from django.urls import path
from apps.categories.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.CategoryAPIView)

urlpatterns = router.urls
