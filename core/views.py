from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.

def home(request):

    ahora = datetime.today() + timedelta(days=1)
    tomorrow = datetime.strftime(ahora, "%Y-%m-%d") 

    return render(request, 'home.html', {
        'title': 'Inicio',
        'fecha': tomorrow   
    })