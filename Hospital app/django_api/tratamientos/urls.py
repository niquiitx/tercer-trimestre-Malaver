from django.urls import path
from .views import *

urlpatterns = [
    path('medicamentos/', MedicamentoListCreate.as_view()),
    path('medicamentos/<int:pk>/', MedicamentoDetail.as_view()),

    path('', TratamientoListCreate.as_view()),
    path('<int:pk>/', TratamientoDetail.as_view()),
]
