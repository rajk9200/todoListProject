from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register-view'),
    path('login/', views.login_view, name='login-view'),
    path('', views.admin_dashboard, name='dashboard'),


]