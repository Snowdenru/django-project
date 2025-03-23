from blog.models import ViewCount


def get_clien_ip(request):
    """
    Получение IP адреса
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARED_FOR")

    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    return ip


def log_user_post(request, post):
    """
    Запись посещения пользователя на страницу с постом
    """
    ip = get_clien_ip(request)

    if request.user.is_authenticated:
        ViewCount.objects.get_or_create(post=post, ip_addres=ip, defaults={'user': request.user.id})
    else:
        ViewCount.objects.get_or_create(post=post, ip_addres=ip)


