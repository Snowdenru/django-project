from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("index/", views.index, name='index'),
    path("", views.post_list, name='post_list'),
    path("detail/<int:pk>/", views.post_detail, name='post_detail'),
    path("book2/", views.book, name='user_book'),
    path("news/", views.news),
    path("user/", views.book),
]
