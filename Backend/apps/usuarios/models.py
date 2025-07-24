from django.db import models

# Create your models here.
class usuarios (models.Model):
    nombre = models.TextField("nombre")
    apellido = models.TextField("apellido")
    rol_id = models.TextField("rol_id")

def __str__(self):
    return f'{self.usuarios}'