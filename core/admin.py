from django.contrib import admin
from .models import Cars 

# Register your models here.

class CarsAdmin(admin.ModelAdmin):
    readonly_fields = ( 'created_at', 'update_at')
    list_display = ('name', 'order', 'created_at')
    ordering = ['order']        


admin.site.register(Cars, CarsAdmin)