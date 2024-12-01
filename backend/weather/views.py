from django.shortcuts import render
from weather.models import City
import requests
# Create your views here.


def list_city_weather(request):
    """Вывод прогноза погоды по выбраным городам"""

    API_KEY = 'cfbc43b5f9bd3167a330f9cbf1413f66'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang=ru"
 
    weather_data = []

    cities = City.objects.all()
    for city in cities:
        city_weather = requests.get(url.format(city, API_KEY)).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
        }

        weather_data.append(weather)

    context = {"weather_data": weather_data}
    return render(request, "weather/list_weather.html", context)
