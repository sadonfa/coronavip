from django.shortcuts import render, get_object_or_404, redirect
from transfer.models import  VehiculosVip
from django.urls import reverse
from .models import Booking
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from coronavip.settings import EMAIL_HOST_USER
import hashlib
import requests
import json

# Create your views here.

def check(request, id=False):
    # d_reserve = VehiculosVip.objects.all()
    transport = VehiculosVip.objects.get(id=request.POST['id'])
    viaje = request.POST['recorrido']

    passengers_list = []
    range_passengers = transport.Number_passengers + 1

    for passengers in range(0, range_passengers):        
        passengers_list.append(passengers)

    if id == False and request.method == 'POST':
        can_comp = 0
        
        if request.POST['name'] == "Van Compartida":
            print("Es compartido ")
            if request.POST['recorrido'] == "ida":
                det_booking = {
                    "name": request.POST['name'],
                    "origen": request.POST['origen'],
                    "destino": request.POST['destino'],
                    "date":  request.POST['date'],
                    "time": request.POST['time'],
                    "id": request.POST['id'],                   
                    "opcion": "transporte",
                    "recorrido": request.POST['recorrido']
                }
                opcion = "transporte"
                can_comp = request.POST['comp-cantidad']
                cash = request.POST['value']
                cash = int(can_comp) * int(cash)
                
                
            else:
                det_booking = {
                    "name": request.POST['name'],
                    "origen": request.POST['origen'],
                    "destino": request.POST['destino'],
                    "date": request.POST['date'],
                    "time": request.POST['time'],
                    "origen_ret": request.POST['origen_ret'],
                    "destino_ret": request.POST['destino_ret'],
                    "date_ret": request.POST['date_return'],
                    "time_ret": request.POST['time_return'],
                    "id": request.POST['id'],                    
                    "opcion": "transporte",
                    "recorrido": request.POST['recorrido']
                }
                opcion = "transporte"
                can_comp = request.POST['comp-cantidad']
                cash = int(request.POST['value']) * 2
                cash = int(can_comp) * int(cash)

        else:
            # no es compartido
            if request.POST['recorrido'] == "ida":
                det_booking = {
                    "name": request.POST['name'],
                    "origen": request.POST['origen'],
                    "destino": request.POST['destino'],
                    "date": request.POST['date'],
                    "time": request.POST['time'],
                    "id": request.POST['id'],
                    "cash" : request.POST['value'],
                    "opcion": "transporte",
                    "recorrido": request.POST['recorrido']
                }       
                opcion = "transporte"
                cash = request.POST['value']
                
                print(det_booking)
                    #realizo arreglo de hora
                t = list(det_booking['time'])   
                # print(len(t))
                if len(t) == 1:
                    v_time = "0" + str(det_booking['time'])
                    # print(tim)
                    segmentar = list(v_time)

                    print(set(segmentar))

                    if set(segmentar) == range(1, 9):
                        segmen = segmentar.insert('0')
                        print(segmen)

                    hora_val = segmentar[0] + segmentar[1]
                    print("hora dividido" + hora_val)

                else:
                    

                    v_time = str(det_booking['time'])
                    # print(tim)
                    segmentar = list(v_time)

                    if set(segmentar) == range(1, 9):
                        segmen = segmentar.insert('0')
                        print(segmen)

                    hora_val = segmentar[0] + segmentar[1]

                
                # v_time = "0"+ str(det_booking['time'])
                

                if int(hora_val) in range(21, 24) or int(hora_val) in range(0, 6):
                    cash = int(request.POST['value']) + 20000
                    print("Se esta enviando este, hora nocturna ")
                    print( cash)
                else:
                    cash = request.POST['value']
                    # print("Se esta enviando este, hora diurna ")
            else:
                #idayvuelta
                det_booking = {
                    "name": request.POST['name'],
                    "origen": request.POST['origen'],
                    "destino": request.POST['destino'],
                    "date": request.POST['date'],
                    "time": request.POST['time'],
                    "time_r": request.POST['time_ret'],
                    "id": request.POST['id'],
                    "cash" : request.POST['value'],
                    "origen_ret": request.POST['origen_ret'],
                    "destino_ret": request.POST['destino_ret'],
                    "date_ret": request.POST['date_ret'],
                    "time_ret": request.POST['time_ret'],
                    "opcion": "transporte",
                    "recorrido": request.POST['recorrido']
                }
                opcion = "transporte"
               
                # print(int(request.POST['value_d']))
                cash = int(request.POST['value']) + int(request.POST['value_d'])
                # print("Este es la hora actual --> " + str(det_booking['time']))
                # print("Este es la hora actual --> " + str(det_booking['time_r']))
                
                # print( "este es el valor de la segunda ruta " + request.POST['value_d'] )


                def Convert(string):
                    li = list(string.split(":"))
                    return li

                list_time = Convert(det_booking['time'])
                hours = int(list_time[0])

                list_time = Convert(det_booking['time_r'])
                hours_r = int(list_time[0])

           
                if int(hours) in range(21, 24) or int(hours) in range(0, 6) :

                    if int(hours_r) in range(21, 24) or int(hours_r) in range(0, 6):
                        cash += 40000
                        # print(f"Se esta enviando este, hora nocturna {cash} ")

                    else:
                        cash += 20000
                        # print(f"Se esta enviando este, hora nocturna {cash}")

                elif int(hours_r) in range(21, 24) or int(hours_r) in range(0, 6) : 
                    if int(hours) in range(21, 24) or int(hours) in range(0, 6):
                        cash += 40000
                        # print(f"Se esta enviando este, hora nocturna {cash} ")

                    else:
                        cash += 20000
                        # print(f"Se esta enviando este, hora nocturna {cash}")

                else:
                    # cash += 40000 
                    print("no hay valor ")

    else:
        det_booking = get_object_or_404(Tours, pk=id)
        cash = det_booking.cash
        opcion = "tour"



    return render(request, 'check.html', {
        'title': 'Informacion de reserva',
        'det_booking': det_booking,
        'cash': cash,
        'opcion': opcion,
        'transports': transport,
        'can_comp': can_comp,
        'passengers_list': passengers_list,
        'recorrido': request.POST['recorrido']

    })

def det_booking(request, opc):


    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        mail = request.POST['mail']  
        cash = request.POST['cash']
        tour = request.POST['tour']
        adults = request.POST['adults']
        opcion = request.POST['opcion']
        aerolinea = request.POST['aerolinea']
        nvuelo = request.POST['nvuelo']

        origen = request.POST['origen']
        destino = request.POST['destino']
        time = request.POST['time']
        date = request.POST['date']
        recorrido = request.POST['recorrido']
        
        if opcion == 'transporte':
            total = int(cash)
        else:   
            total = int(adults) * int(cash)        
        
        print(recorrido)

        if recorrido == 'ida':
            air_r="None"
            nair_r="None"                             
            origen_ret="None"
            destino_ret="None"
            date_ret="2021-01-01"
            hora_ret="00:00"
        else:
            air_r=request.POST['aerolinea_r']
            nair_r=request.POST['nvuelo_r']                            
            origen_ret=request.POST['origen_ret']
            destino_ret=request.POST['destino_ret']
            date_ret=request.POST['date_ret']
            hora_ret=request.POST['time_ret']   


        booking = Booking(
            name=name,
            phone=phone,
            mail=mail,
            cash=cash,
            tour=tour,
            adults=adults, 
            air=aerolinea,
            nair=nvuelo,
            air_r=air_r,            
            nair_r=nair_r,                  
            origen=origen,
            destino=destino,
            checkin=date,
            hora=time,                
            origen_ret=origen_ret,
            destino_ret=destino_ret,
            date_ret=date_ret,
            hora_ret=hora_ret,
            opcion=opcion,
            recorrido=recorrido,
            total=total,   
        )

        
        booking.save()            
    

    return render(request, 'det_booking.html', {
        'title': 'Detalles de Reserva',
        'total': total,
        'booking': booking,      
        'opcion': opcion,
        'recorrido': recorrido
    })

def answer_booking(request, id=False):
    
    id_wompi = request.GET['id']
    # tour = get_object_or_404(Tours, id=53)


    #URL_API =  "https://sandbox.wompi.co/v1/transactions/" + id_wompi
    URL_API =  "https://production.wompi.co/v1/transactions/" + id_wompi

    response = requests.get(URL_API)

    if response.status_code == 200:
          tour = response.json()
          for t in tour:
                print(t)
    else:
          tour = []

    id_booking = tour['data']['reference']
    id_booking = id_booking.lstrip('CV0')
              
    
    booking = Booking.objects.get(id=id_booking ) 

    if response.status_code == 200:

        subject = 'Nueva reserva de ' + booking.name 
        template = render_to_string(
            'correo.html',
            context={
                'nbooking': tour['data']['reference'],
                'name': booking.name,      
                'correo': booking.mail,
                'content': booking.name,
                'phone' : booking.phone,
                'cash' : booking.cash,
                'tour' : booking.tour,
                'checkin' : booking.checkin,
                'hora': booking.hora,
                'origen': booking.origen,
                'destino': booking.destino, 
                "origen_ret":booking.origen_ret,
                "destino_ret":booking.destino_ret,
                "date_ret":booking.date_ret,
                "hora_ret":booking.hora_ret,
                'adults' : booking.adults,
                'vuelo': booking.air,
                'nvuelo': booking.nair ,
                'vuelo_r': booking.air_r,
                'nvuelo_r': booking.nair_r,
                'total' : booking.total,
                'opcion' : booking.opcion,
                'recorrido': booking.recorrido,
                'method' : tour['data']['payment_method']['type'] ,
                'card':tour['data']['payment_method']['extra']['name'] ,
                'card_type': tour['data']['payment_method']['extra']['card_type'],
                'data': tour['data']['finalized_at'],

                },
            )        

        message = EmailMultiAlternatives(
            subject, #Titulo
            "This is an important message.",
            EMAIL_HOST_USER, #Remitente
            ["coronaserviciosvip@gmail.com", booking.mail]) #Destinatario

        message.attach_alternative(template, 'text/html')
        message.send()  

    return render(request, 'respuesta.html', {
        'title': 'confirmacion reserva',     
        'id': tour['data']['reference'],
        'tour': tour,
        'booking': booking          
    })

