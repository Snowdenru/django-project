from django.shortcuts import redirect


def index(request):
    return redirect('blog:post_list')
