from django.db import models


# После того, как создали новую таблицу, необходимо выполнить команду
# python manage.py makemigrations
# python manage.py migrate


class City(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name
    

