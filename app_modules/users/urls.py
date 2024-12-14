from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from app_modules.users import views

router = DefaultRouter()


urlpatterns = [
    path("register/",views.UserRegisterView.as_view(),name="register_user"),
    path("login/",views.UserLoginView.as_view(),name="login")
]
