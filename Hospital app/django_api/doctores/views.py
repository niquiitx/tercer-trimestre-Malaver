from rest_framework import generics
from .models import Doctor, Especialidad
from .serializers import DoctorSerializer, EspecialidadSerializer

# --- Especialidades ---
class EspecialidadListCreate(generics.ListCreateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class EspecialidadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

# --- Doctores ---
class DoctorListCreate(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


