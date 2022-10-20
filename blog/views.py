from django.shortcuts import redirect, render
from django.contrib.auth import logout as django_logout
from .models import Publicaciones
from .form import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required

def inicio(request): #user
    return render(request, "general/index.html")

def sobreNosotras(request): #user
    return render(request, "general/sobreNosotras.html")

class ListaPublicaciones(ListView):
    template_name = 'publicaciones/publicaciones_list.html'
    model = Publicaciones

class DetallePublicacion(DetailView):
    template_name = 'publicaciones/publicacion_detail.html'
    model = Publicaciones


class CrearPublicacion(CreateView):
    template_name = 'publicaciones/agregarPaginas_form.html'
    model = Publicaciones
    success_url = "/pages/edit"
    fields = ["imagen", "titulo","subtitulo","cuerpo","autor","fecha"]


class ActualizarPublicacion(UpdateView):
    template_name = 'publicaciones/agregarPaginas_form.html'
    model = Publicaciones
    success_url = "/pages/edit"
    fields = ["titulo","subtitulo","cuerpo","autor","fecha"]


class BorrarPublicacion(DeleteView):
    template_name = 'publicaciones/eliminarPaginas_confirm_delete.html'
    model = Publicaciones
    success_url = "/pages/edit"


class ListaPublicacionesEdicion(ListView):
    
    template_name = 'publicaciones/verPaginas_list.html'
    model = Publicaciones


#cuenta

#mostrar opciones de perfil
@login_required(login_url='/accounts/login')
def perfil(request): #user

    usuario = request.user

    return render(request, "user/infoCuenta.html", {"usuario": usuario})

#cerrar mi sesión
@login_required(login_url='/accounts/login')
def logout(request): #user

    django_logout(request)

    return redirect("inicio")

#vista ver los usuarios
@login_required(login_url='/accounts/login')
def vistaUsuarios(request):

    usuarios = User.objects.all()

    return render(request, "user/verUsuarios_list.html", context={"usuarios": usuarios})

#vista eliminar los usuarios
@login_required(login_url='/accounts/login')
def eliminarUsuarios(request, username):

    usuario = User.objects.get(username=username)
    usuario.delete()

    usuarios = User.objects.all()

    return render(request, "user/verUsuarios_list.html", context={"usuarios": usuarios})


#vista para agregar mi avatar
@login_required(login_url='/accounts/login')
def editarUsuarios(request, username_data): #admin

    usuario = User.objects.get(username=username_data)

    usuarioActual = request.user

    print(request.method)

    if request.method == 'POST':

        form = EditarUsuario(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email=info["email"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.set_password=info["password1"]

            usuario.save()

            return redirect("perfil")

    else:

        form = EditarUsuario(initial={
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name
        })

    return render(request, "user/editarUsuarios.html", {"formulario": form, "usuario": usuarioActual})

@login_required(login_url='/accounts/login')
def editarUsuarioIndividual(request, username_data): #admin

    usuario = User.objects.get(username=username_data)

    if request.method == 'POST':

        form = EditarUsuario(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email=info["email"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.set_password=info["password1"]

            usuario.save()

            return redirect("editarUsuarios")

    else:

        form = EditarUsuario(initial={
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name
        })

    return render(request, "user/editarUsuarioIndividual.html", {"formulario": form})

#avatar

#vista para agregar mi avatar
@login_required(login_url='/accounts/login')
def agregarAvatar(request):

    usuarioActual = request.user

    if request.method == "POST":

        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            avatar = Avatar(usuario = usuarioActual,
                imagen = form.cleaned_data["imagen"])

            avatar.save()

            return redirect("perfil")

    else:

        form = AvatarForm()

    return render(request, "user/agregarAvatar.html", {"formulario": form, "usuario": usuarioActual})

