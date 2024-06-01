from .views import *
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('upload/', UploadView.as_view(), name='upload'),
]
