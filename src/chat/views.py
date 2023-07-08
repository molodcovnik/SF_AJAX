import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from accounts.models import Profile
from .models import Chat

def index(request):
    #return render(request, "flatpages/default.html")
    return render(request, "chat/index.html")


# @login_required
def room(request, room_name):
    return render(request, "chat/room.html", {
        "room_name": mark_safe(json.dumps(room_name)),
        "username": mark_safe(json.dumps(request.user.username))
        })



def random_code():
    random.seed()
    return random.randint(1000, 9999)

def create_chat(request, invited_username):
    creator = request.user.username
    chat_name = f'{str(creator)}_{str(invited_username)}'
    print(chat_name)
    Chat.objects.create(chat_name=chat_name)
    return render(request, "chat/room.html", {
        "room_name": mark_safe(json.dumps(chat_name)),
        "username": mark_safe(json.dumps(request.user.username))
    })






# def create_chat(request, pk):
#     creator = request.user.username
#     invited = Profile.objects.get(id=pk)
#     invited_username = invited.user.username
#     chat_name = f'{str(creator)}_{str(invited_username)}'
#     print(chat_name)
#     Chat.objects.create(chat_name=chat_name)
#     return render(request, "chat/room.html")
    # return render(request, "chat/room.html", {
    #     "room_name": mark_safe(json.dumps(chat_name)),
    #     "username": mark_safe(json.dumps(request.user.username))
    # })
