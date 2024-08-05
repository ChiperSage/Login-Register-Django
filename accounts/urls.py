# accounts/urls.py

from django.urls import path
from .views import RegisterView, LoginView, UserCreateView, UserUpdateView, UserListView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('list/', UserListView.as_view(), name='user_list'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
