import requests
from django.shortcuts import get_object_or_404, redirect, render
from weather.forms import CityForm
from weather.models import City

# Create your views here.


def list_city_weather(request):
    """Вывод прогноза погоды по выбраным городам"""

    API_KEY = 'cfbc43b5f9bd3167a330f9cbf1413f66'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang=ru"
 
    weather_data = []

    cities = City.objects.all()
    form = CityForm()
    for city in cities:
        city_weather = requests.get(url.format(city, API_KEY)).json()
        weather = {
            'pk': city.pk,
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
        }

        weather_data.append(weather)
    

    context = {"weather_data": weather_data, "form": form}
    return render(request, "weather/list_weather.html", context)



def сity_create(request):
    """Добавление нового города"""

    if request.method =='POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weather:list_city_weather')
        

def city_delete(request, pk):
    city = get_object_or_404(City, pk=pk)
    city.delete()
    return redirect('weather:list_city_weather')
    
