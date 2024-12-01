from django.urls import path
from weather import views

app_name = "weather"

urlpatterns = [
    path("", views.list_city_weather, name='list_city_weather'),
]
