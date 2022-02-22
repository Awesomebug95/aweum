from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import *


class User(AbstractUser):
    """
    Model User.
    """
    phone = CharField(
        max_length=15,
        unique=True,
    )
    telegram = CharField(
        max_length=50,
        unique=True
    )
    country = CharField(
        max_length=50
    )
    photo = ImageField(
        upload_to='users/'
    )

    # TODO: create post, departament, groups.

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"
        ordering = ('last_name',)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
