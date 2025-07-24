from django.db import models

# Create your models here.
class pagos (models.Model):
    hora_salida = models.TextField("hora_salida")
    pago_total = models.TextField("pago_total")
    automovil_id = models.TextField("automovil_id")
    factura = models.TextField("factura")

def __str__(self):
    return f'{self.pagos}'