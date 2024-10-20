from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list),
    path("detail/<int:pk>/", views.post_detail, name='post_detail'),
    path("book2/", views.book, name='user_book'),
    path("news/", views.news),
    path("user/", views.book),
]
