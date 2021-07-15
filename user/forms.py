from django import forms
from .models import User


class LoginForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
