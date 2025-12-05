from django.db import models

class Habitacion(models.Model):
    numero = models.CharField(max_length=10, unique=True)  # o IntegerField si prefieres
    tipo = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=20, default='Disponible')  # Disponible / Ocupada / Limpieza

    def __str__(self):
        return f"Habitación {self.numero} - {self.tipo}"
