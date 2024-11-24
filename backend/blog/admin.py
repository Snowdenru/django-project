from django.contrib import admin

from .models import Post, Category

# Создание супер пользователя для работы в админке
# python manage.py createsuperuser

admin.site.register(Post)
admin.site.register(Category)