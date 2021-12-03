from django.db import models

from django.contrib.auth.models import User


class Task(models.Model):
    """Общая шаблонная инфа по задаче"""
    title = models.CharField(max_length=128)
    description = models.TextField()
    verifiability = models.BooleanField()
    experience = models.IntegerField()
    in_course = models.BooleanField()
    achievement = ...


class UserTask(models.Model):
    """Инфа по задаче, персонализированная для конкретного юзера"""
    class Status(models.TextChoices):
        confirmed = 'S1', 'Подтверждено'
        cancelled = 'S2', 'Отклонено'

    deadline = models.DateTimeField()
    perfect_deadline = models.DateTimeField()
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='user_tasks',
        related_query_name='user_task',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_tasks',
        related_query_name='user_task',
    )
    responsible = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='responsible_tasks',
        related_query_name='responsible_task',
    )

    # Оценка, статус и описание.
    status = models.CharField(max_length=2, choices=Status.choices)
    estimation = models.SmallIntegerField()
    description = models.TextField()
