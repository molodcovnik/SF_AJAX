from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth.models import User
from .serializers import UsersSerializer



class UsersList(generics.ListAPIView):
    serializer_class = UsersSerializer

    def get_queryset(self):
        return User.objects.all()