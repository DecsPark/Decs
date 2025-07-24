from django.db import models

# Create your models here.
class ingreso (models.Model):
    precio = models.TextField("precio")
    servicio_id = models.TextField("servicio_id")

def __str__(self):
    return f'{self.ingreso}'