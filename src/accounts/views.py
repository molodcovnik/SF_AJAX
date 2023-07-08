from typing import Any
from django.db import models
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth.models import User
from .models import Profile
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
# from django.views.generic.edit import FormMixin

from .forms import SignUpForm




class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'accounts/signup.html'
    

class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'accounts/create_profile.html'
    fields = ['about_me', 'photo']


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get_success_url(self, **kwargs):
    #     return reverse_lazy('profile', kwargs={'pk': self.get_object().profile.id})


class ProfileView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class ProfilesView(ListView):
    model = Profile
    template_name = 'accounts/profiles.html'
    context_object_name = 'profiles'