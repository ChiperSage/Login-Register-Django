# accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import RegisterForm, LoginForm, UserCreateForm, UserUpdateForm, ProfileForm
from .models import User

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'accounts/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'accounts/login.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class UserCreateView(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, 'accounts/user_create.html', {'form': form})

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, 'accounts/user_create.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class UserUpdateView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, user_id=pk)
        form = UserUpdateForm(instance=user)
        return render(request, 'accounts/user_update
