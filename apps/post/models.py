from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(
        max_length=255

    )

    descriptions = models.CharField(
        max_length=255
    )

    image = models.ImageField(
        upload_to="Image"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"