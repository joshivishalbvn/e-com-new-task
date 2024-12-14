from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from app_modules.products import views

router = DefaultRouter()
router.register(r"products",views.ProductViewSet,basename="product")
router.register(r"products/(?P<product_id>\d+)/images",views.ProductImagesViewSet,basename="product-images")


urlpatterns = [
]

urlpatterns += router.urls