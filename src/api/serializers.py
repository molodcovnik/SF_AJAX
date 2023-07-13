from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Profile
from chat.models import Chat, Message

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'profile',)


class UsersSerializerChatList(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',)


class ChatListSerializers(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Chat
        fields = ('id', 'chat_name', 'members',)


class UserChatListSerializers(serializers.ModelSerializer):
    username = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    photo = serializers.FileField(source='profile.photo')
    

    class Meta:
        model = Chat
        fields = ('id', 'username', 'profile', 'photo',)


class MessageSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='__str__')

    class Meta:
        model = Message
        fields = ('id', 'author', 'content', 'time', )


class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    username = serializers.CharField(source='user.username')
    class Meta:
        model = Profile
        fields = ('id', 'about_me', 'photo', 'user', 'username',)

