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

    def __str__(self):
        return self.title
