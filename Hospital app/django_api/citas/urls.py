from django.urls import path
from .views import *
from .views import home

urlpatterns = [
    path('inicio', home, name='home'),
    path('', CitaListCreate.as_view()),
    path('<int:pk>/', CitaDetail.as_view()),
]
