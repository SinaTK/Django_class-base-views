from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class UserLogin(LoginView):
    template_name = 'accounts/login.html'

class UserLogout(LogoutView):
    next_page = reverse_lazy('home:home')