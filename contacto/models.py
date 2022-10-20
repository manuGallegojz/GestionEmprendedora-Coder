from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return f"User: {self.nombre} -- Password: {self.asunto}"