from django.db import models

# Create your models here.

class Cars(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    desciption = models.CharField(max_length=200, verbose_name="Descripcion")
    Number_passengers = models.IntegerField(default=0, verbose_name="Cantidad de pasajeros")
    amount_luggage = models.IntegerField(default=0, verbose_name="Cantidad de equipaje")
    image = models.ImageField(default='null', verbose_name= 'Imagen', upload_to='vehiculos_vip')
    image1 = models.ImageField(default='null', verbose_name= 'Imagen1', upload_to='vehiculos_vip')
    image2 = models.ImageField(default='null', verbose_name= 'Imagen2', upload_to='vehiculos_vip')
    image3 = models.ImageField(default='null', verbose_name= 'Imagen3', upload_to='vehiculos_vip')
    order = models.IntegerField(default=0, verbose_name="Orden")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Editado el")

    class Meta:
        verbose_name="Carros de lujo"
        verbose_name_plural="Carros de lujo"
        ordering=['order']

    def __str__(self):
        return self.name