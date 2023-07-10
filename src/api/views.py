from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth.models import User
from chat.models import Chat, Message
from rest_framework import permissions
from .serializers import UsersSerializer, ChatListSerializers, UsersSerializerChatList


class UsersList(generics.ListAPIView):
    serializer_class = UsersSerializer

    def get_queryset(self):
        return User.objects.all()


class ChatList(generics.ListCreateAPIView):
    serializer_class = ChatListSerializers
    # permission_classes= 

    def get_queryset(self):
        return Chat.objects.all()

    def get_post(self, serializers, chat_name, members):
        serializers.save(chat_name=chat_name,
                         members=members)


class ChatListUser(generics.ListAPIView):
    serializer_class = ChatListSerializers
    permission_classes = [permissions.AllowAny]

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        # return Chat.objects.filter(members=user)
        return Chat.objects.filter(members=self.kwargs['pk'])


