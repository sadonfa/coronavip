from django.db import models
from django.utils import timezone

# Create your models here.

class Booking(models.Model):                
    name = models.CharField(max_length=200, verbose_name="Nombre")
    phone  = models.TextField(max_length=100, verbose_name="Nombre")
    mail = models.EmailField(max_length=200, verbose_name="Correo")
    cash = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Valor", default=0)
    tour = models.CharField(max_length=200, verbose_name="Tours")
    adults  = models.CharField(max_length=100, verbose_name="Adultos")
    air = models.CharField(max_length=  200, verbose_name="Aerolinea")
    nair = models.CharField(max_length=200, verbose_name="numero de vuelo")
    air_r = models.CharField(default="None",  max_length=200, verbose_name="Aerolinea retorno")
    nair_r = models.CharField(default="None", max_length=200, verbose_name="numero de vuelo retorno")
    origen = models.CharField(default="null", max_length=200, verbose_name="Origen")
    destino = models.CharField(default="null", max_length=200, verbose_name="Destino")
    hora = models.TimeField(verbose_name="Hora",  default=timezone.now  )     
    checkin = models.DateField(default=0, verbose_name="Checkin" )
    
    origen_ret = models.CharField(default="null", max_length=200, verbose_name="Origen de retorno")
    destino_ret = models.CharField(default="Null", max_length=200, verbose_name="Destino de retorno")
    date_ret = models.DateField(default=0, verbose_name="Fecha de retorno" )
    hora_ret = models.TimeField(default=0, verbose_name="Hora de retorno")   

    total = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="total", default=0)
    opcion = models.CharField(max_length=100, default="null", verbose_name="Opcion")
    recorrido = models.CharField(max_length=100, default="null", verbose_name="Recorrido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado el")

    def __str__(self):
        return f'{self.name}' 

    def get_id_formateado(self):
        return str(self.pk).zfill(6)