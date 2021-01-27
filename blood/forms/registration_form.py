from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import TextInput, PasswordInput, CharField, EmailInput
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    password1 = CharField(
        widget=PasswordInput(
            attrs={'class': 'form-control py-4', 'placeholder': 'Password'}),
    )
    password2 = CharField(
        widget=PasswordInput(
            attrs={'class': 'form-control py-4', 'placeholder': 'Confirm Password'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Username'}),
            'email': EmailInput(attrs={'class': 'form-control py-4', 'placeholder': 'Email Address'})
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
