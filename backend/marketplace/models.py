from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings


# После того, как создали новую таблицу, необходимо выполнить команду
# python manage.py makemigrations
# python manage.py migrate

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    """Таблица отзывов"""
    text = models.TextField("Текст отзыва")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Product(models.Model):
    STATUS_CHOICES = [
        (1, 'Опубликован'),
        (2, 'В разработке'),
        (3, 'Архив'),
        (4, 'Удалено'),
    ]

    name = models.CharField("Название товара", max_length=200)
    description = models.TextField("Описание товара", blank=True, null=True)
    image = models.ImageField(
        "Изображение товара",
        blank=True,
        null=True,
        upload_to="images/product/%Y/%m/%d/",
        validators=[
            FileExtensionValidator(allowed_extensions=("png", "jpg", "webp", "gif"))
        ],
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField("Статус", choices=STATUS_CHOICES)
    price = models.IntegerField("Стоимость") 
    comment = models.ManyToManyField(Feedback,verbose_name="Отзыв", blank=True)

    def __str__(self):
        return self.name
 
