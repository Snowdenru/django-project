from django.shortcuts import render
from system.models import UserStat
from blog.models import Post


def static_user_dashboard(request):
    data = UserStat.objects.all().order_by('date')
    data_post = Post.objects.all()

    context = {
        'data':data,
        'data_post': data_post
    }

    return render(request, 'dashboard/static_user.html', context)
