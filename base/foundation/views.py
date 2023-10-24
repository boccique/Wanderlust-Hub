from django.shortcuts import render
from .models import RegisteredUser


def tempfile(request):
    users = RegisteredUser.objects.all
    context = {'users': users}
    return render(request, 'tempfile.html', context)


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):
    users = RegisteredUser.objects.all
    context = {'users': users}
    return render(request, 'register.html', context)
