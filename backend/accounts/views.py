from accounts.forms import SignUpForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/sign_up.html"

