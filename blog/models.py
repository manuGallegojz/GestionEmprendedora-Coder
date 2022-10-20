from email.mime import image
from http import server
from django.db import models
from django.contrib.auth.models import User

class Publicaciones(models.Model):
    imagen = models.ImageField(upload_to="blog_imagenes",null=True, blank=True)
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=150)
    fecha = models.CharField(max_length=200)

    def __str__(self):
        return f"Titulo: {self.titulo} -- Autor: {self.autor} -- Fecha: {self.fecha}"

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to="avatar",null=True, blank=True)
