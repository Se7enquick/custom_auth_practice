from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView

from .forms import UserRegisterForm


class SignUpView(CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
