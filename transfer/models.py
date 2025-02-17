from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VehiculosVip(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    tipo = models.CharField(max_length=200, verbose_name="Tipo")
    Number_passengers = models.IntegerField(default=0, verbose_name="Cantidad de pasajeros")
    amount_luggage = models.IntegerField(default=0, verbose_name="Cantidad de equipaje")
    image = models.ImageField(default='null', verbose_name= 'Imagen', upload_to='vehiculos_vip')
    order = models.IntegerField(default=0, verbose_name="Orden")
    user = models.ForeignKey(User, editable=False, verbose_name="Usuario", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado el")

    class Meta:
        verbose_name="Vehiculo VIP"
        verbose_name_plural="Vehiculos VIP"
        ordering=['order']

    def __str__(self):
        return self.name