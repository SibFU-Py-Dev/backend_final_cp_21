from django.contrib.auth.models import User
from django.db import models

from project.models import Project


class Employee(models.Model):
    class Roles(models.TextChoices):
        STUDENT = 'ST', 'Новый сотрудник'
        TEACHER = 'TC', 'Наставник'
        ADMIN = 'AD', 'Руководитель проекта'

    role = models.CharField(verbose_name='Роль', choices=Roles.choices)
    img = models.ImageField(
        upload_to='users/avatars/',
        null=True,
        verbose_name='Аватар',
    )
    user = models.OneToOneField(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="employee",
    )
    mobile_phone = models.CharField(
        max_length=17,
        help_text='Номер мобильного телефона',
    )
    city_phone = models.CharField(
        max_length=7,
        help_text='Номер городского телефона',
    )
    hobby = models.TextField()
    skills = models.TextField()
    interests = models.TextField()
    # achievements = ...
    experience = models.IntegerField()
    project = models.ForeignKey(
        to=Project,
        on_delete=models.SET_NULL,
        related_name='employees',
        related_query_name='employee',
        null=True,
        blank=True,
    )
