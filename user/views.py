from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate


def homepage(request):
    ...
# Listing.objects.all()


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    form = LoginForm()
    return render(request, 'login', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
