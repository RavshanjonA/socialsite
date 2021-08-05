from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import UserCreateForm


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'