from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistration(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField( )
    password1 = forms.PasswordInput()
    password2 = forms.CharField()
    test = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']