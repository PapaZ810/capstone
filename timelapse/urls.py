from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/', IndexView.as_view(), name='index'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('images/', ImagesView.as_view(), name='images'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
