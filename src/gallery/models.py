from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    photo = models.ImageField(
        null=False,
        blank=False,
        upload_to='photos',
        verbose_name='Фотография'
    )

    description = models.CharField(
        null=False,
        blank=False,
        max_length=256,
        verbose_name='Подпись'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    # RELATIONS
    author = models.ForeignKey(
        to=get_user_model(),
        related_name='photos',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    favourites = models.ManyToManyField(
        blank=True,
        to=get_user_model(),
        related_name='favourites',
        verbose_name='Избранное',
    )

    def __str__(self):
        return f'Author: "{self.author}", Description: "{self.description}", Created: {self.created_at}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографий'


