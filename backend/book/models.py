from django.db import models


class Book(models.Model):
    title = models.CharField("Название книги", max_length=256)
    description = models.TextField("Описание книги", blank=True, null=True)
    author = models.CharField("Автор книги", max_length=256)
    genre = models.CharField("Жанр книги", max_length=256)
    publication_year = models.IntegerField("Год публикации")
    is_read = models.BooleanField('Прочитана ли книга?', default=False)
    img = models.CharField("URL адресс на обложку книги", max_length=1024, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
