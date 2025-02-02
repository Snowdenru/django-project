from django.urls import path
from todo import views

app_name = "todo"

urlpatterns = [
    path("", views.ListTodoView.as_view(), name='todo_list'),
    path("<int:todo_id>/delete", views.delete, name='delete'),
    path("<int:todo_id>/update", views.update, name='update'),
    path("add/", views.add, name='add'),
    
]
