from django.shortcuts import render
from django.views.generic import *


# Create your views here.

class IndexView(TemplateView):
    template_name = 'timelapse/index.html'


class UploadView(TemplateView):
    template_name = 'timelapse/upload.html'

