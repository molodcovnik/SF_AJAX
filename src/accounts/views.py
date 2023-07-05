from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from accounts.forms import SignUpForm



class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'accounts/signup.html'

