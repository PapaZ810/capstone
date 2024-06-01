from django import forms


class UploadForm(forms.Form):
    image = forms.ImageField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
