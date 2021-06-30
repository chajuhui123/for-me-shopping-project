from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, TextInput, PasswordInput
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'length', 'shoulder', 'chest', 'waist', 'rise', 'hem']
        widget = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 150px; height: 50px;',
                'placeholder': '아이디 입력',
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'style': 'width: 150px; height: 50px;',
                'placeholder': '비밀번호 입력',
            }),
        }