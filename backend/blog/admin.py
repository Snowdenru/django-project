from django.contrib import admin

from .models import Post

# Создание супер пользователя для работы в админке
# python manage.py createsuperuser

admin.site.register(Post)
