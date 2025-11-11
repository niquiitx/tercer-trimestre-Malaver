from django.urls import path
from .views import *

urlpatterns = [
    path('', CitaListCreate.as_view()),
    path('<int:pk>/', CitaDetail.as_view()),
]
