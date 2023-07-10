from django.urls import path
from .views import UsersList, ChatList, ChatListUser



urlpatterns = [
    path('users/', UsersList.as_view()),
    path('chats/', ChatList.as_view()),
    path('chat_list/<int:pk>/', ChatListUser.as_view()),
]