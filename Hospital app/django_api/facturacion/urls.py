from django.urls import path
from .views import *

urlpatterns = [
    path('', FacturaListCreate.as_view()),
    path('<int:pk>/', FacturaDetail.as_view()),
]
