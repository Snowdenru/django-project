from django.contrib import admin

from .models import Post, Category, ViewCount

# Создание супер пользователя для работы в админке
# python manage.py createsuperuser

admin.site.register(Post)
admin.site.register(Category)


@admin.register(ViewCount)
class ViewCountAdmin(admin.ModelAdmin):
    pass