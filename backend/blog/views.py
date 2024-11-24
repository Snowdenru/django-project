from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post, Category


def index(request):

    context = {
        "title": "Тестовая страница",
        "description": "Подробное описание страницы",
        "code": "Тут какой-то код",
        "created_at": "2024-11-01",
        'tags': ['обучение', 'программирование', 'python', 'oop']
    }
    return render(request, "blog/index.html", context)


def post_list(request):
    """
    Представления для получения всех постов
    """
    filter_category = request.GET.get('category')
    if filter_category:
        posts = Post.objects.filter(published_date__isnull=False, category__name=filter_category)
    else:
        posts = Post.objects.filter(published_date__isnull=False)
    category = Category.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts, "category": category})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


# def index(request):
#     return HttpResponse("Hello Django!")


def book(request):
    return HttpResponse("Книга 1")


def news(request):
    return HttpResponse("Новость 1")


# def main(request):

#     all_posts = Post.objects.all()

#     context = {"user_name": "Denis", "message": "Hello World", "posts": all_posts}
#     return render(request, "blog/main.html", context)
