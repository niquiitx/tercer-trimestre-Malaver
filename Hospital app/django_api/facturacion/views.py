from rest_framework import generics
from .models import Factura
from .serializers import FacturaSerializer
from django.shortcuts import render

def home(request):
    citas_lista = Factura.objects.all()
    return render(request, 'facturacion/inicio.html', {"facturacion": citas_lista})


class FacturaListCreate(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class FacturaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
