from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
]
