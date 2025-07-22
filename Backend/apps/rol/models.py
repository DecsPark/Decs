from django.db import models

# Create your models here.
class rol (models.models):
    id = models.texfield("id")
    nombre = models.texfield("nombre")

def __str__(self):
    return f'{self.rol}'
        
