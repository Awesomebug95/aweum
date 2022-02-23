from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'watcher',
            'executor',
            'deadline',
            'project',
        )
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'watcher': 'Наблюдатели',
            'executor': 'Исполнитель',
            'deadline': 'Дедлайн',
            'project': 'Проект',
        }
        help_texts = {
            'title': 'Название задачи',
            'description': 'Опишите задачу',
            'watcher': 'Выберите наблюдателей',
            'executor': 'Выберите ответственного',
            'deadline': 'Когда задача должна быть завершена?',
            'project': 'Проект к которому относится задача',
        }
