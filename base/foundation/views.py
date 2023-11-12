from django.shortcuts import render
from .models import RegisteredUser
from .models import Something
from .forms import RegisteredUserForm
from django.http import HttpResponseRedirect


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
    subbmited = False
    if request.method == 'POST':
        form = RegisteredUserForm(request.POST)
        if form.is_valid():
            form.save()

    form = RegisteredUserForm
    context = {'form': form}
    return render(request, 'register.html', context)


def sometext(request):
    sometexts = Something.objects.all
    context = {'sometexts': sometexts}
    return render(request, 'sometext.html', context)
