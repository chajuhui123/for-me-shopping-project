from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, TextInput, PasswordInput
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'length', 'shoulder', 'chest', 'waist', 'rise', 'hem']
        