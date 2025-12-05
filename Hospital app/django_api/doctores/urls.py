from django.urls import path
from .views import *

urlpatterns = [
    path('especialidades/', EspecialidadListCreate.as_view()),
    path('especialidades/<int:pk>/', EspecialidadDetail.as_view()),

    path('', DoctorListCreate.as_view()),
    path('<int:pk>/', DoctorDetail.as_view()),
]
