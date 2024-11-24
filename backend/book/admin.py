from django.contrib import admin

from .models import Book

# Создание супер пользователя для работы в админке
# python manage.py createsuperuser

admin.site.register(Book)