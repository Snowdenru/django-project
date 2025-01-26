from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    """
    Модуль обратной связи
    """

    subject = models.CharField(max_length=255, verbose_name="Тема письма")
    email = models.EmailField(max_length=255, verbose_name="Электронный адрес")
    content = models.TextField(verbose_name="Содержимое письма")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='+'
    )

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-time_create']

    def __str__(self):
        return self.subject
    