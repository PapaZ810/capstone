from .views import *
from django.urls import path

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/', IndexView.as_view(), name='index'),
    path('upload/', UploadView.as_view(), name='upload'),
]
