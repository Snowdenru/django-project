from django.shortcuts import render
from system.models import UserStat


def static_user_dashboard(request):
    data = UserStat.objects.all().order_by('date')

    context = {
        'data':data
    }

    return render(request, 'dashboard/static_user.html', context)
