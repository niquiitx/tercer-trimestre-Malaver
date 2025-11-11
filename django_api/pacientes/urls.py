from django.urls import path
from .views import *

urlpatterns = [
    path('habitaciones/', HabitacionListCreate.as_view()),
    path('habitaciones/<int:pk>/', HabitacionDetail.as_view()),

    path('', PacienteListCreate.as_view()),
    path('<int:pk>/', PacienteDetail.as_view()),

    path('ingresos/', IngresoListCreate.as_view()),
    path('ingresos/<int:pk>/', IngresoDetail.as_view()),
]
