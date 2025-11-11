from django.db import models
from pacientes.models import Paciente
from doctores.models import Doctor

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    dosis = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Tratamiento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    duracion_dias = models.IntegerField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Tratamiento de {self.paciente} con {self.medicamento}"

