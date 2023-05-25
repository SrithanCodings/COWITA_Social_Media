from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    class Meta:
        model = User
        first_name = forms.CharField(max_length=255)
        last_name = forms.CharField(max_length=255)
        email = forms.EmailField(max_length=255)
        phone = forms.IntegerField()
        dob = forms.DateField()
        password1 = forms.PasswordInput()
        password2 = forms.PasswordInput()


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.PasswordInput()
