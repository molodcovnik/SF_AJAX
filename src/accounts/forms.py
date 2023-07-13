from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Profile
from django.core.mail import send_mail
from django.forms import Textarea


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


# class CustomSignupForm(SignUpForm):
#     def save(self, request):
#         user = super().save(request)
#         profile = Profile.objects.create(user=user)
#         profile.save()
#         return profile

