from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    MyTokenObtainPairView,
    UserProfileView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    UserListView,
    UserListByIDView,
    ChatGemini, ReadFileView, VideoDownloader
)

#api/auth/users
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('profile/', UserProfileView.as_view(), name='profile'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password-reset-confirm'),

    path('users/', UserListView.as_view(), name='users'),
    path('user/<pk>', UserListByIDView.as_view(), name='users-id'),
    path('profile/', UserProfileView.as_view(), name='profile'),


    path('chatai/', ChatGemini.as_view(), name='chat-ai'),
    path('read-file/', ReadFileView.as_view(), name='read-file'),
    path('download-video/', VideoDownloader.as_view(), name='video-downloader'),

]