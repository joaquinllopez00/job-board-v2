from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data["username"], password=data["password"], email=data["email"], bio=data["bio"])
    form = SignUpForm()
    return render(request, 'signup.html', {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=['password'])
            login(request, user)
            return HttpResponseRedirect(reverse('home.html'))
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home.html'))
