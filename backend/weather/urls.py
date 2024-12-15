from django.urls import path
from weather import views

app_name = "weather"

urlpatterns = [
    path("", views.list_city_weather, name='list_city_weather'),
    path("city/create/", views.сity_create, name='сity_create'),
    path("city/<int:pk>/delete/", views.city_delete, name='city_delete'),
]
