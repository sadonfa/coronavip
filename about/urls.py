from django.urls import path
from . import views

urlpatterns = [
    path('nosotros', views.about, name="about"),
]
