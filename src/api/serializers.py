from rest_framework import serializers
from django.contrib.auth.models import User
from chat.models import Chat, Message

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username',)


class UsersSerializerChatList(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',)


class ChatListSerializers(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Chat
        fields = ('id', 'chat_name', 'members',)

