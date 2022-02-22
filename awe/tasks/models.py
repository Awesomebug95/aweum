from django.db.models import *

from projects.models import Project
from users.models import User


class Task(Model):
    title = CharField(
        max_length=150,
        blank=False
    )
    description = CharField(
        max_length=800,
        blank=False
    )
    author = ForeignKey(
        User,
        on_delete=PROTECT,
        related_name='tasks',
        verbose_name='Автор'
    )
    watcher = ManyToManyField(
        User,
        blank=True,
        related_name='watchers',
        verbose_name='Наблюдатели',
        help_text='Выберите наблюдателей'
    )
    executor = ForeignKey(
        User,
        on_delete=PROTECT,
        related_name='executor',
        verbose_name='Исполнитель',
        help_text='Выберите исполнителя'
    )
    deadline = DateField(
        blank=False
    )
    status = BooleanField(
        default=True
    )
    project = ForeignKey(
        Project,
        on_delete=CASCADE,
        related_name='projects',
        verbose_name='Проект',
        help_text='Выберите проект'
    )
    created_at = DateTimeField(auto_now_add=True)
    edited_at = DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title[:25]
