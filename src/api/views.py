from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth.models import User
from chat.models import Chat, Message
from accounts.models import Profile
from rest_framework import permissions
from .serializers import (UsersSerializer, ChatListSerializers, UsersSerializerChatList,
                          UserChatListSerializers, MessageSerializers, ProfileSerializers)
from rest_framework.decorators import api_view


class UsersList(generics.ListAPIView):
    serializer_class = UsersSerializer

    def get_queryset(self):
        user = self.request.user.id
        admin = User.objects.get(id=1).id
        list = [user, admin]
        return User.objects.all().exclude(id__in=list)


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializers

    def get_queryset(self):
        return Profile.objects.all()


class ChatList(generics.ListCreateAPIView):
    serializer_class = ChatListSerializers
    # permission_classes= 

    def get_queryset(self):
        return Chat.objects.all()

    def get_post(self, serializers, chat_name, members):
        serializers.save(chat_name=chat_name,
                         members=members)

    # def put(self, serializers, chat_name, members):
    #     serializers.save(chat_name=chat_name,
    #                      members=members)

class ChatUpdate(generics.UpdateAPIView):
    serializer_class = ChatListSerializers

    def patch(self, request, *args, **kwargs):
        chat_name = self.kwargs['room_name']
        user_id = self.request.data['members']
        print(user_id)
        user = User.objects.get(id=user_id)
        chat = Chat.objects.get(chat_name=chat_name)
        chat.members.add(user)
        chat.save()
        return Response(status.HTTP_202_ACCEPTED)

class ChatDetailDestroyView(generics.DestroyAPIView):
    serializer_class = ChatListSerializers

    def get_queryset(self):
        return Chat.objects.get(chat_name=self.kwargs['room_name'])
    def delete(self, *args, **kwargs):
        chat_name = self.kwargs['room_name']
        chat = Chat.objects.get(chat_name=chat_name)
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ChatListUser(generics.ListAPIView):
    serializer_class = ChatListSerializers
    permission_classes = [permissions.AllowAny]

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        # return Chat.objects.filter(members=user)
        return Chat.objects.filter(members=self.kwargs['pk'])




class UserChatListView(generics.ListAPIView):
    serializer_class = UserChatListSerializers

    def get_queryset(self, *args, **kwargs):
        chat_name = self.kwargs['room_name']
        chat = Chat.objects.get(chat_name=chat_name)
        print(chat.members.filter(chat=chat))
        return chat.members.filter(chat=chat)


class LastMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializers

    def get_queryset(self, *args, **kwargs):
        chat_name = self.kwargs['room_name']
        chat = Chat.objects.get(chat_name=chat_name)
        print(chat.messages.filter(chat=chat))
        return chat.messages.filter(chat=chat)
