from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    class Genders(models.TextChoices):
        MALE = 'male', 'Мужчина'
        FEMALE = 'female', 'Женщина'

    # Required
    email = models.EmailField(
        verbose_name='Почта',
        unique=True,
        null=False,
        blank=False,
    )

    # Required
    avatar = models.ImageField(
        null=False,
        blank=False,
        upload_to='avatars',
        verbose_name='Аватар',
        default='avatars/default.png'
    )

    about = models.TextField(
        max_length=2048,
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
