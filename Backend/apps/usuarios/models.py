from django.db import models

# Create your models here.
class usuarios (models.models):
    id = models.texfield("id")
    nombre = models.texfield("nombre")
    apellido = models.texfield("apellido")
    rol_id = models.texfield("rol_id")

def __str__(self):
    return f'{self.usuarios}'