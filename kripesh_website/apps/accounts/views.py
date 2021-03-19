from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'