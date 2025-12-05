from django.db import models
from pacientes.models import Paciente, Ingreso

class Factura(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    ingreso = models.ForeignKey(Ingreso, on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Factura #{self.id} - {self.paciente}"
