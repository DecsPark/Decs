from django.db import models

# Create your models here.
class automovil (models.models):
    id = models.texfield("id")
    placa = models.texfield("placa")
    usuarios_id = models.texfield("usuarios_id")
    fecha_ingreso = models.texfield("fecha_ingreso")

def __str__(self):
    return f'{self.automovil}'