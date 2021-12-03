from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    # img = models.ImageField(upload_to='images/', default='empty.jpg', null=True, verbose_name='Изображение')
    user = models.OneToOneField(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="employee"
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
    # experience = ...
