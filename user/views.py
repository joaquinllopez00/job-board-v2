from django import template
from django.shortcuts import redirect, render, reverse, HttpResponseRedirect
from job.models import Listing
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.generic import RedirectView


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
                return HttpResponseRedirect(request.GET.get("next", reverse("home")))
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def profile_view(request, username):
    user = User.objects.filter(username=username)
    listings = Listing.objects.filter(user=user).order_by('-post_date')
#   notifications = views.notification_count_view(request)
    if request.user.is_authenticated:
        fave_jobs = Listing.objects.filter(favorited_by=request.user)
    else:
        fave_jobs = []
#   Utilize context = {'user': user, 'listings': listings, 'notifications': notifications, 'fave_job': fave_job} once Notification model/views are built
    return render(request, 'profile.html', {'user': user, 'listings': listings, 'fave_jobs': fave_jobs})


@login_required
def edit_profile(request, id):
    prof = User.objects.get(id=id)
    if request.method == "POST":
        form = EditProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            prof.name = data["name"]
            prof.username = data["username"]
            prof.email = data["email"]
            prof.bio = data["bio"]
            prof.experience = data["experience"]
            prof.skills = data["skills"]
            prof.contact_num = data["contact_num"]
            prof.save()
        return HttpResponseRedirect(reverse("home"))
    form = EditProfileForm(initial={
        'name': prof.name,
        'username': prof.username,
        'email': prof.email,
        'bio': prof.bio,
        'experience': prof.experience,
        'skills': prof.skills,
        'contact_num': prof.contact_num,
    })
    return render(request, "profile.html", {"form": form})


class logout_view(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self):
        logout(self.request)
        return reverse("home")
