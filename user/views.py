from django import template
from django.shortcuts import redirect, render, reverse, HttpResponseRedirect
from job.models import Listing
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.template import RequestContext


def homepage(request):
    listings = Listing.objects.all()
    return render(request, 'home.html', {'listings': listings})


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data.get("username"), password=data.get("password"), email=data.get('email'))
    form = SignUpForm()
    return render(request, 'signup.html', {"form": form})


def login_view(request):
    template_name = "login.html"
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get('username'), password=data.get('password'), email=data.get('email'))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", "/"))
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Class based view


class logout_view(View):
    def get(self, request):
    logout(request)
    return HttpResponseRedirect(reverse('home.html'))
