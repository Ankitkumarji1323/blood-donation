from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'placeholder': 'Username', id: 'username', 'required': True,
               'autofocus': True}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control py-4', 'placeholder': 'Password', id: 'password', 'required': True}))
    remember_me = forms.BooleanField(required=False)
