from django.contrib import admin
from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/<str:login_type>/', LoginView.as_view()),
]
