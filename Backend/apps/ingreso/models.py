from django.db import models

# Create your models here.
class ingreso (models.models):
    id = models.texfield("id")
    precio = models.texfield("precio")
    servicio_id = models.texfield("servicio_id")

def __str__(self):
    return f'{self.ingreso}'