from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    create_at = models.DateTimeField('Дата создания', auto_now_add=True)
    update_at = models.DateTimeField('Дата изменения', auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title