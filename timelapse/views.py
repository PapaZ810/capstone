import json
from .forms import *
from django.views.generic import *
from django.shortcuts import render
from capstone.settings import MEDIA_ROOT
from django.middleware.csrf import get_token
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'timelapse/index.html'


def handle_uploaded_file(f):
    with open(MEDIA_ROOT.__str__().replace('\\', '/') + '/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def send_csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})


def get_instructions(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            send_instructions(request, data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'This endpoint only accepts POST requests'})


def send_instructions(request, json_data):
    return JsonResponse({'pictures': json_data})


@method_decorator(csrf_exempt, name='dispatch')
class UploadView(LoginRequiredMixin, FormView):
    login_url = '/'
    template_name = 'timelapse/upload.html'
    form_class = UploadForm
    success_url = '/home/'

    def form_valid(self, form):
        if self.request.method == 'POST':
            form = UploadForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                handle_uploaded_file(self.request.FILES['image'])
                x = form.save(commit=False)
                x.user = self.request.user
                x.save()
                return render(self.request, 'timelapse/index.html')
            else:
                print(form.errors)
                print(form.cleaned_data)
        else:
            form = UploadForm()


class LoginView(FormView):
    template_name = 'timelapse/login.html'
    form_class = LoginForm
    success_url = '/home/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error('password', "Invalid username or password")
            return self.form_invalid(form)


class ImagesView(LoginRequiredMixin, ListView):
    login_url = '/'
    model = Image
    template_name = 'timelapse/images.html'
    context_object_name = 'images'

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'timelapse/dashboard.html'
