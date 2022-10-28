from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuario(UserCreationForm):

    username = forms.CharField(label = "Nombre de Usuario",max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    first_name = forms.CharField(label = "Nombre",max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    last_name = forms.CharField(label = "Apellido",max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]