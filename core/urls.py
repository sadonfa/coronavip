from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('inicio/', views.home, name="home"),
    path('contacto/', views.contact, name="contact"),
    path('enviar/', views.sendform, name="sendform"),
]
