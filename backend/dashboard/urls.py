from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("static_user/", views.static_user_dashboard, name='static_user_dashboard'),
 
]
