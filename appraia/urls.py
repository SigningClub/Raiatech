from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('login/', views.logar_usuario, name="logar_usuario"),
    path('', views.main, name="main"),
    path('create_user/', views.create_user, name="create_user")
]