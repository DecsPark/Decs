from django.db import models

# Create your models here.
class automovil (models.Model):
    placa = models.TextField("placa")
    usuarios_id = models.TextField("usuarios_id")
    fecha_ingreso = models.TextField("fecha_ingreso")

def __str__(self):
    return f'{self.automovil}'