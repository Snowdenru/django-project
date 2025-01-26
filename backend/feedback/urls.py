from django.urls import path
from feedback import views

app_name = "feedback"

urlpatterns = [
    path("", views.send_message_user, name='send_message_user'),
     
]
