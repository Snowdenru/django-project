from django.shortcuts import render
from book.models import Book


def list_book(request):
    """Вывод списка всех книг"""

    books_1 = Book.objects.all()
    return render(request, "book/book_list.html", context={"books": books_1})


def book_detail(request, pk):

    book = Book.objects.get(pk=pk)

    return render(request, "book/book_detail.html", context={"book": book})