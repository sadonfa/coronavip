from django.shortcuts import render
from .models import VehiculosVip

# Create your views here.

def detail(request):

    if request.method == 'POST':
        # >>>>>>>--- comente unas variables por aqui ---<<<<<<<
        viaje = request.POST['viaje']
        print(viaje)
        if viaje == "ida":  
            trayecto = {
                'start':  request.POST['start_of_route'],
                'end':  request.POST['end_of_route'],
                'date':  request.POST['date'],
                'time':  request.POST['time'] ,
                'distance':  request.POST['distance'] ,
                'duration':  request.POST['duration'] ,
            }   
           
        elif viaje == "idayvuelta":
            trayecto = {
                'start': request.POST['start_of_route'],
                'end':  request.POST['end_of_route'],
                'date':  request.POST['date'],
                'time':  request.POST['time'],
                'start_ret':  request.POST['start_of_route_return'],
                'end_ret':  request.POST['end_of_route_return'],
                'date_ret': request.POST['date_return'],
                'time_ret': request.POST['time_return'],
            }   

        print(trayecto)

    return render(request, "detail.html", {
        'title': "Detalles",
        'trayecto': trayecto,
        'recorrido': viaje,
    })  


def transfer(request):

    vehiculosvip = VehiculosVip.objects.all()
    compartido = VehiculosVip.objects.filter(name="Van Compartida")
    recorrido = request.POST['recorrido']

    print(recorrido)

    def Convert(string):
        li = list(string.split(":"))
        return li

    if recorrido == "ida":
        dat_trayecto = {
                'start':  request.POST['start_of_route'],
                'end':  request.POST['end_of_route'],
                'date':  request.POST['date'],
                'time':  request.POST['time'] ,
                'distance':  request.POST['distance'] ,
                'duration':  request.POST['duration'] ,
            }   
         

        list_time = Convert(request.POST['time'])
        hours = int(list_time[0])

        st_duracion = int(request.POST['duration'])/60
        dura = int(round(st_duracion))

        st_distancia = int(request.POST['distance'])*10**-3
        kilometros = int(round(st_distancia))           


        if int(kilometros) in range(1, 12):
            print(f"correcto son {kilometros}km")
            valor_trayecto = {
                'vehiculo_lujo': 350000,  # multiplicar por personas
                'camioneta': 360000,  # locale.currency(45000, grouping=True),
                'lujo': 380000,  # locale.currency(85000, grouping=True),
                'mini_van_lujo': 360000,
                'van_lujo': 360000,  # locale.currency(150000, grouping=True),
            }
        elif int(kilometros) in range(13, 30):
            print(f"correcto son {kilometros}km")
            valor_trayecto = {
                'vehiculo_lujo': 450000,
                'camioneta': 460000,  # locale.currency(60000, grouping=True),
                'lujo': 480000,  # locale.currency(100000, grouping=True),
                'mini_van_lujo': 460000,
                'van_lujo': 460000,  # locale.currency(180000, grouping=True),
            }
        elif int(kilometros) in range(31, 58):
            print(f"correcto son {kilometros}km")
            valor_trayecto = {
                'vehiculo_lujo': 1100000,  # locale.currency(10000, grouping=True),
                'camioneta': 1100000,  # locale.currency(190000, grouping=True),
                'lujo': 1300000,  # locale.currency(280000,  grouping=True),               
                'mini_van_lujo': 1200000, # locale.currency(400000, grouping=True),               
                'van_lujo': 1400000  # locale.currency(500000, grouping=True),
            }
        else:
            print("Incorrecto")

    else:
        dat_trayecto = {
            'date' : request.POST['date'],
            'time' : request.POST['time'],
            "date_ret": request.POST['date_return'],
            "time_ret": request.POST['time_return'],   
            'start' : request.POST['start_of_route'],
            'end' : request.POST['end_of_route'],
            "start_r": request.POST['start_of_route_return'],
            "end_r": request.POST['end_of_route_return'],
            'distance' : request.POST['distance'],
            'duration' : request.POST['duration'],  
            'distance_ret' : request.POST['distance_ret'],
            'duration_ret' : request.POST['duration_ret'],
        }

       

        list_time = Convert(request.POST['time'])
        hours = int(list_time[0])

        st_distancia = int(request.POST['distance'])*10**-3
        kilometros = int(round(st_distancia))

        st_duracion = int(request.POST['duration'])/60
        dura = int(round(st_duracion))

        rt_distance = int(request.POST['distance_ret'])*10**-3
        kilm = int(round(rt_distance))

        rt_duracion = int(request.POST['duration_ret'])/60
        dura_rt = int(round(rt_duracion))

        if int(kilometros) in range(1, 12):
            
            valor_trayecto = {
                'compartido': 15000,  # multiplicar por personas
                'standar': 55000,  # locale.currency(45000, grouping=True),
                'mini_van': 120000,  # locale.currency(85000, grouping=True),
                # locale.currency(100000, grouping=True),
                'van_standar': 160000,
                'micro_bus': 220000,  # locale.currency(120000, grouping=True),
                'buseta': 250000,  # locale.currency(170000, grouping=True),
                'bus': 350000,  # locale.currency(200000, grouping=True),
                'SUV': 150000,  # locale.currency(150000, grouping=True),
            }
        elif int(kilometros) in range(13, 30):
            valor_trayecto = {
                'compartido': 30000,
                'standar': 85000,  # locale.currency(60000, grouping=True),
                'mini_van': 150000,  # locale.currency(100000, grouping=True),
                # locale.currency(120000, grouping=True),
                'van_standar': 190000,
                'micro_bus': 250000,  # locale.currency(150000, grouping=True),
                'buseta': 300000,  # locale.currency(190000, grouping=True),
                'bus': 450000,  # locale.currency(260000, grouping=True),
                'SUV': 180000,  # locale.currency(180000, grouping=True),
            }
        elif int(kilometros) in range(31, 58):
            valor_trayecto = {
                'compartido': 35000,  # locale.currency(10000, grouping=True),
                'standar': 450000,  # locale.currency(190000, grouping=True),
                'mini_van': 650000,  # locale.currency(280000,  grouping=True),
                # locale.currency(400000, grouping=True),
                'van_standar': 750000,
                'micro_bus': 900000,  # locale.currency(480000, grouping=True),
                'buseta': 1050000,  # locale.currency(530000, grouping=True),
                'bus': 1200000,  # locale.currency(600000, grouping=True),
                'SUV': 550000  # locale.currency(500000, grouping=True),
            }
        else:
            print("Incorrecto")

        if int(kilm) in range(1, 12):
            v_trayecto_dos = {
                'compartido': 15000,  # multiplicar por personas
                'standar': 55000,  # locale.currency(45000, grouping=True),
                'mini_van': 120000,  # locale.currency(85000, grouping=True),
                # locale.currency(100000, grouping=True),
                'van_standar': 160000,
                'micro_bus': 220000,  # locale.currency(120000, grouping=True),
                'buseta': 250000,  # locale.currency(170000, grouping=True),
                'bus': 350000,  # locale.currency(200000, grouping=True),
                'SUV': 150000,  # locale.currency(150000, grouping=True),
            }
        elif int(kilm) in range(13, 30):
            v_trayecto_dos = {
                'compartido': 30000,
                'standar': 85000,  # locale.currency(60000, grouping=True),
                'mini_van': 150000,  # locale.currency(100000, grouping=True),
                # locale.currency(120000, grouping=True),
                'van_standar': 190000,
                'micro_bus': 250000,  # locale.currency(150000, grouping=True),
                'buseta': 300000,  # locale.currency(190000, grouping=True),
                'bus': 450000,  # locale.currency(260000, grouping=True),
                'SUV': 180000,  # locale.currency(180000, grouping=True),
            }
        elif int(kilm) in range(31, 58):
            v_trayecto_dos = {
                'compartido': 35000,  # locale.currency(10000, grouping=True),
                'standar': 450000,  # locale.currency(190000, grouping=True),
                'mini_van': 650000,  # locale.currency(280000,  grouping=True),
                # locale.currency(400000, grouping=True),
                'van_standar': 750000,
                'micro_bus': 900000,  # locale.currency(480000, grouping=True),
                'buseta': 1050000,  # locale.currency(530000, grouping=True),
                'bus': 1200000,  # locale.currency(600000, grouping=True),
                'SUV': 550000  # locale.currency(500000, grouping=True),
            }
        else:
            print("Incorrecto_2")
                        

    return render(request, 'transfer.html', {
        'title': 'Transporte',
        'recorrido': recorrido,
        'v_trayecto': valor_trayecto,
        'vehiculosvip': vehiculosvip,
        'dat_trayecto': dat_trayecto,
    })      


