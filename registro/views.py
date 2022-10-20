from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Cuenta
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import RegistroUsuario

def registrarse(request):

    if request.method == "POST":

        form = RegistroUsuario(request.POST)

        if form.is_valid():

            # username = form.cleaned_data["username"]
            form.save()
            return redirect("inicio")

    else:

        form = RegistroUsuario()

    return render(request, "registro.html", {"formulario": form})
