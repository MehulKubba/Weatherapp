from django.shortcuts import render
import urllib.request
import json

def index(request):
    data = {}  
    
    if request.method == 'POST':
        city = request.POST.get('city', None)
        if city:  
            try:
                source = urllib.request.urlopen(
                    'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=3cfdf49e5e7fc57bba074e46d6bcda7d'
                ).read()
                list_of_data = json.loads(source)
                data = {
                    "country_code": str(list_of_data['sys']['country']),
                    "coordinate": str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
                    "temp": str(list_of_data['main']['temp']) + ' °C',
                    "pressure": str(list_of_data['main']['pressure']),
                    "humidity": str(list_of_data['main']['humidity']),
                    'main': str(list_of_data['weather'][0]['main']),
                    'description': str(list_of_data['weather'][0]['description']),
                    'icon': list_of_data['weather'][0]['icon'],
                }
            except Exception as e:
                data = {'error': str(e)}
        else:
            data = {'error': 'No city provided'}

    return render(request, "app/index.html", data)
