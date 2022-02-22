from django.db import models
from django.db.models import *

from users.models import User


class Project(Model):
    """
    Model Project.
    """
    title = CharField(
        max_length=150,
        unique=True
    )
    description = CharField(
        max_length=800
    )
    author = ForeignKey(
        User,
        on_delete=PROTECT,
        related_name='projects',
        verbose_name='Автор'
    )
    workers = ManyToManyField(
        User,
        blank=True,
        related_name='workers',
        verbose_name='Работники',
        help_text='Выберите работников'
    )
    deadline = DateField(
        blank=False
    )
    admins = ManyToManyField(
        User,
        related_name='admins',
        verbose_name='Администраторы'
    )
    status = BooleanField(
        default=True
    )
    created_at = DateTimeField(auto_now_add=True)
    edited_at = DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ('created_at',)

    def __str__(self):
        return self.title[:25]
