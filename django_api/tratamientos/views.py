from rest_framework import generics
from .models import Medicamento, Tratamiento
from .serializers import MedicamentoSerializer, TratamientoSerializer

# --- Medicamentos ---
class MedicamentoListCreate(generics.ListCreateAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class MedicamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


# --- Tratamientos ---
class TratamientoListCreate(generics.ListCreateAPIView):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class TratamientoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer
