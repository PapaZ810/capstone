from django import forms
from .models import Image


class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['user', 'image']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
