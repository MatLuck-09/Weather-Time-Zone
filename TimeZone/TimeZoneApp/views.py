from django.shortcuts import render, HttpResponse

#from client import Client
from .client import ClimaClient

# Create your views here.
def home(request):
    try:
        if request.method == 'POST':
            city = request.POST.get('city')
            response = ClimaClient().get_clima_info(city)
            
            if response is None:
                return HttpResponse("Bad Request", status=400)

            else:
                data = response
                temp_celsius = data['main']['temp'] - 273.15
                temp_max_celsius = data['main']['temp_max'] - 273.15
                temp_min_celsius = data['main']['temp_min'] - 273.15
                feels_like_celsius = data['main']['feels_like'] - 273.15
                traducciones_clima = {
                    'Thunderstorm': 'Tormenta',
                    'Drizzle': 'Llovizna',
                    'Rain': 'Lluvia',
                    'Snow': 'Nieve',
                    'Mist': 'Niebla',
                    'Clear': 'Despejado',
                    'Clouds': 'Nublado',
                }
                clima_en_ingles = data['weather'][0]['main']
                clima_en_espanol = traducciones_clima.get(clima_en_ingles, clima_en_ingles)

                return render(request, 'TimeZoneApp/toGo.html', {
                    'city': data['name'],
                    'main': clima_en_espanol,
                    'temp': temp_celsius,
                    'max': temp_max_celsius,
                    'min': temp_min_celsius,
                    'feels': feels_like_celsius,
                })
        return render(request, 'TimeZoneApp/home.html', {})
    
    except Exception as error:
        return HttpResponse("Error en la solicitud", status=400)
