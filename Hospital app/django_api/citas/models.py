from django.db import models
from pacientes.models import Paciente
from doctores.models import Doctor

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=50, default="Pendiente")

    def __str__(self):
        return f"Cita de {self.paciente} con {self.doctor} el {self.fecha}"
