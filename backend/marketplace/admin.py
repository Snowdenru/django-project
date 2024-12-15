from django.contrib import admin

from marketplace import models 

# Создание супер пользователя для работы в админке
# python manage.py createsuperuser

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Feedback)
