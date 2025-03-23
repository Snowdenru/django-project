from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import FileExtensionValidator


# После того, как создали новую таблицу, необходимо выполнить команду
# python manage.py makemigrations --name "create_post"
# python manage.py migrate


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        "Превью поста",
        blank=True,
        null=True,
        upload_to="images/thumbnails/%Y/%m/%d/",
        validators=[
            FileExtensionValidator(allowed_extensions=("png", "jpg", "webp", "gif"))
        ],
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_view_count(self):
        """
        Возвращает количество просмотров для данного поста
        """
        return self.viewcount_set.count()

    def __str__(self):
        return self.title


class ViewCount(models.Model):
    """
    Модель просмотров для постов
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    ip_addres = models.GenericIPAddressField(verbose_name='Ip адрес')
    viewed_on = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')

    class Meta:
        ordering = ('-viewed_on',)
        verbose_name = 'Просмотр'
        verbose_name_plural = 'Просмотры'

    def __str__(self):
        return self.post.title

