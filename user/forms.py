from django import forms
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    name = forms.CharField(max_length=150)
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    name = forms.CharField(max_length=150)
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

# class EditProfileForm(forms.Form):
