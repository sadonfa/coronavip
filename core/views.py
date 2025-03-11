from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Cars
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from coronavip.settings import EMAIL_HOST_USER

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

def contact(request):
   

    return render(request, "contact.html", {
        'title': 'Contactos'
    })

def sendform(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        mail = request.POST['mail']
        info = request.POST['info']

    subject = 'Comentario de ' + fullname 
    template = render_to_string(
            'formulario.html',
            context={                
                'name': fullname,      
                'correo': mail,
                'info': info,               

                },
            )        

    message = EmailMultiAlternatives(
            subject, #Titulo
            "This is an important message.",
            EMAIL_HOST_USER, #Remitente
            ["coronaserviciosvip@gmail.com", mail]) #Destinatario

    message.attach_alternative(template, 'text/html')
    message.send()  
    
    return render(request, "home.html")