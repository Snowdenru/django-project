from django.db import models
from django.conf import settings


class UserStat(models.Model):
    cnt_user = models.IntegerField("Кол-во пользователей")
    date = models.DateField("Дата")


# class UserLog(models.Model):
#     ACTION_CHOISES = (
#         (1, 'Переход на главную')
#     )
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
#     )
#     action_id = models.IntegerField('ID дейсвия', choices=ACTION_CHOISES)
#     datetime = models.DateTimeField("Время действия")


#     class Meta():
#         verbose_name = 'Лог'
#         verbose_name_plural = 'Логи'
