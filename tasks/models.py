from django.db import models

from django.contrib.auth.models import User


class Task(models.Model):
    """Общая шаблонная инфа по задаче"""
    title = models.CharField(max_length=128)
    description = models.TextField()
    verifiability = models.BooleanField()
    experience = models.IntegerField()
    achievement = ...


class UserTask(models.Model):
    """Инфа по задаче, персонализированная для конкретного юзера"""
    class Status(models.TextChoices):
        confirmed = 'S1', 'Подтверждено'
        cancelled = 'S2', 'Отклонено'


    deadline = models.DateTimeField(null=True, blank=True)
    perfect_deadline = models.DateTimeField(null=True, blank=True)
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='user_tasks',
        related_query_name='user_task',
        null=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_tasks',
        related_query_name='user_task',
        null=True,
    )
    responsible = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='responsible_tasks',
        related_query_name='responsible_task',
        null=True,
    )

    # Оценка, статус и описание.
    status = models.CharField(max_length=2, choices=Status.choices, null=True, blank=True)
    estimation = models.SmallIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
