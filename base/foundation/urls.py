from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path('register/', views.register, name="register"),
    path('test/', views.tempfile, name="test"),
    path('sometext/', views.sometext, name="sometext"),
    path('user/', views.user_page, name="user")
]
