from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from app_modules.orders import views

router = DefaultRouter()
router.register(r"orders",views.OrderViewSet,basename="order")


urlpatterns = [
]

urlpatterns += router.urls
