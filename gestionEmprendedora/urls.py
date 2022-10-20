from django.contrib import admin
from django.urls import path

from blog.views import *
from registro.views import *
from login.views import *
from contacto.views import *

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required

urlpatterns = [

    #general

    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('about/', sobreNosotras, name="sobreNosotras"),

    #publicaciones

    path('pages/', ListaPublicaciones.as_view(), name="paginas"),
    path('pages/detail/<int:pk>', DetallePublicacion.as_view(), name="DetallePublicacion"),
    path('pages/edit', login_required(ListaPublicacionesEdicion.as_view(), login_url='/accounts/login'), name="paginasEditar"),
    path('pages/edit/paginasCrear', login_required(CrearPublicacion.as_view(), login_url='/accounts/login'), name="paginasCrear"),
    path('pages/edit/paginasEliminar/<int:pk>', login_required(BorrarPublicacion.as_view(), login_url='/accounts/login'), name="paginasEliminar"),
    path('pages/edit/paginasEditar/<int:pk>', login_required(ActualizarPublicacion.as_view(), login_url='/accounts/login'), name="paginasEditar"),

    #cuenta

    path('accounts/signup', registrarse, name="registrarse"),
    path('accounts/login', inicioSesion, name="login"),
    path('accounts/profile', perfil, name="perfil"),
    path('accounts/logout', logout, name="logout"),
    path('users/edit', vistaUsuarios, name="editarUsuarios"),
    path('accounts/edit/<username_data>/', editarUsuarios, name="editarMiUsuario"),
    path('accounts/singleEdit/<username_data>/', editarUsuarioIndividual, name="editarMiUsuarioIndividual"),
    path('accounts/delete/<username>', eliminarUsuarios, name="eliminarMiUsuario"),

    #avatar

    path('accounts/avatar', agregarAvatar, name="agregarAvatar"),

    #mensajes

    path('contacto/', contacto, name="contacto"),
    path('accounts/mensajes', listarMensajes, name="misMensajes"),
    path('accounts/mensajes/delete/<id>', eliminarMensajes, name="mensajeEliminar"),
    path('accounts/mensajes/read/<id>', leerMensajes, name="mensajeLeer"),

]

urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)