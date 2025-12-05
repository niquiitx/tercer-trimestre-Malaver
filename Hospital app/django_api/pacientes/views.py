from rest_framework import generics
from .models import Paciente, Habitacion, Ingreso
from .serializers import PacienteSerializer, HabitacionSerializer, IngresoSerializer

# --- Habitaciones ---
class HabitacionListCreate(generics.ListCreateAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

class HabitacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer


# --- Pacientes ---
class PacienteListCreate(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


# --- Ingresos ---
class IngresoListCreate(generics.ListCreateAPIView):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer

class IngresoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer
