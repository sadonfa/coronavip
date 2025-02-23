from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Cars

# Create your views here.

def home(request):

    cars = Cars.objects.all()

    ahora = datetime.today() + timedelta(days=1)
    tomorrow = datetime.strftime(ahora, "%Y-%m-%d") 

    return render(request, 'home.html', {
        'title': 'Inicio',
        'fecha': tomorrow,
        'cars': cars,
    })