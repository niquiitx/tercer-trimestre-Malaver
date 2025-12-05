from rest_framework import generics
from .models import Cita
from .serializers import CitaSerializer
from django.shortcuts import render

def home(request):
    citas_lista = Cita.objects.all()
    return render(request, 'citas/inicio.html', {"citas": citas_lista})


class CitaListCreate(generics.ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class CitaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
