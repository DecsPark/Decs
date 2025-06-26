from django.db import models

# Create your models here.
class pagos (models.models)
    id = models.texfield("id")
    hora_salida = models.texfield("hora_salida")
    pago_total = models.texfield("pago_total")
    automovil_id = models.texfield("automovil_id")
    factura = models.texfield("factura")

    def_str_(Self):
        return f'{Self.pagos}'
