from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class EditarUsuario(UserCreationForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control sanserif'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control sanserif'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control sanserif'}))
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control sanserif'}))
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control sanserif'}))

    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]

class AvatarForm(forms.ModelForm):

    imagen = forms.FileField(label='', widget=forms.FileInput(attrs={'class': 'form-control'}))
    
    class Meta:

        model = Avatar
        fields = ["imagen"]
