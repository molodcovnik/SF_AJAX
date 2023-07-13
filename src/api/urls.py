from django.urls import path
from .views import UsersList, ChatList, ChatListUser, UserChatListView, LastMessagesView, ChatDetailDestroyView, ProfileListView



urlpatterns = [
    path('users/', UsersList.as_view()),
    path('chats/', ChatList.as_view()),
    path('profiles/', ProfileListView.as_view()),
    path('chat_list/<int:pk>/', ChatListUser.as_view()),
    path('chat_user/<str:room_name>/', UserChatListView.as_view()),
    path('chat/<str:room_name>/', ChatDetailDestroyView.as_view()),
    path('chat_messages/<str:room_name>/', LastMessagesView.as_view()),
    
]