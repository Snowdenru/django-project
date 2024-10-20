from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post



def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False)

    return render(request, 'blog/post_list.html',{
        "posts": posts
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html',{
        "post": post
    })



def index(request):
    return HttpResponse("Hello Django!")


def book(request):
    return HttpResponse("Книга 1")


def news(request):
    return HttpResponse("Новость 1")


def main(request):

    all_posts = Post.objects.all()

    context = {"user_name": "Denis", "message": "Hello World", "posts": all_posts}
    return render(request, "blog/main.html", context)
