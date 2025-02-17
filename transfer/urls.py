from django.urls import path
from . import views

urlpatterns = [
    path('detalles/', views.detail, name="detail" ),
    path('transporte/', views.transfer, name="transfer"),
]
