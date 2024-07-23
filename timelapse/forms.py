from django import forms
from .models import Image


class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['user', 'image']
        widgets = {
            'user': forms.TextInput(),
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
