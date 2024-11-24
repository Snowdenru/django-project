from django.urls import path
from book import views

app_name = "book"

urlpatterns = [
    path("", views.list_book, name='list_book'),
    path("books-detail/<int:pk>/", views.book_detail, name='book_detail'),

]
