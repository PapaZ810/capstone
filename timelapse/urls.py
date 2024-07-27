from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/', IndexView.as_view(), name='index'),
    path('upload/', UploadView.as_view(), name='upload'),
    path('images/', ImagesView.as_view(), name='images'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('csrf/', send_csrf, name='csrf'),
    path('instructions/', get_instructions, name='instructions'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
