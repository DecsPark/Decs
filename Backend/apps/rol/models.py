from django.db import models

# Create your models here.
class rol (models.Model):
    nombre = models.TextField("nombre")

def __str__(self):
    return f'{self.rol}'
        
