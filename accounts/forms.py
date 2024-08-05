# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import User, Role, Group

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role', 'group']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'role', 'group']

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'role', 'group', 'is_active', 'is_staff']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'role', 'group']
