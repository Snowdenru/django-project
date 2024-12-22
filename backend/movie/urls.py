from django.urls import path
from movie import views

app_name = "movie"

urlpatterns = [
    path("", views.premier_movie, name='premier_movie'),
]
