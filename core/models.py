from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

class FormContacto(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=150)