from django.urls import path
from .views import SignUp, CreateProfilePageView, ProfileView, ProfilesView, ProfileEdit, UserFirstNameEditView

app_name = 'accounts'

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit', ProfileEdit.as_view(), name='profile_update'),
    path('profile/<int:pk>/edit_fname', UserFirstNameEditView.as_view(), name='profile_update_first_name'),

    path('profiles/', ProfilesView.as_view(), name='profiles'),
]