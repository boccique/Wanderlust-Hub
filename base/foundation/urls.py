from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('about/', views.services, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.services, name="contact"),
    path('register/', views.register, name="register"),
]
