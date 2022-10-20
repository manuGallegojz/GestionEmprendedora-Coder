from django.shortcuts import render
from .forms import ContactoFormulario
from .models import Contacto
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def contacto(request):
    
    if request.method == "POST":

        form = ContactoFormulario(request.POST)

        if form.is_valid():

            usuario = request.user

            info = form.cleaned_data

            mensaje = Contacto(nombre = usuario.username,
            email = usuario.email,
            asunto = info["asunto"],
            mensaje = info["mensaje"])

            mensaje.save()

            return render(request, "contacto.html", {"formulario": form, "mensaje": "Tu formulario fue enviado con éxito"})

    else:

        form = ContactoFormulario()

    return render(request, "contacto.html", {"formulario": form})


def listarMensajes(request):

    mensajes = Contacto.objects.all()

    context = {"mensajes": mensajes}

    return render(request, "mensajes_list.html", context)

@login_required
def eliminarMensajes(request, id): #admin

    msj = Contacto.objects.get(id=id)
    msj.delete()

    mensajes = Contacto.objects.all()

    context = {"mensajes": mensajes}

    return render(request, "mensajes_list.html", context)

@login_required
def leerMensajes(request, id): #admin

    msj = Contacto.objects.get(id=id)

    context = {"mensaje": msj}

    return render(request, "mensaje_detail.html", context)