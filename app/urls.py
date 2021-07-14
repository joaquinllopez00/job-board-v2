"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import request
from django.urls import path
from user import views
from job import views as job_views
from django.conf.urls import (handler404, handler500)

handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.homepage, name="home"),
    path('create/', job_views.create_listing_view.as_view(), name="create_listing"),
    path('listing/<int:listing_id>/', job_views.listing_detail_view.as_view(), name="listing_detail"),
    path("signup/", views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
