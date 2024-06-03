from .forms import *
from django.shortcuts import render
from django.views.generic import *
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'timelapse/index.html'


class UploadView(LoginRequiredMixin, FormView):
    login_url = '/'
    template_name = 'timelapse/upload.html'
    form_class = UploadForm
    success_url = '/index/'

    def form_valid(self, form):
        return super(UploadView, self).form_valid(form)


class LoginView(FormView):
    template_name = 'timelapse/login.html'
    form_class = LoginForm
    success_url = '/home/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print('god help me')

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            print("Invalid username or password")
            form.add_error('password', "Invalid username or password")
            return self.form_invalid(form)


