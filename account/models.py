from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# mobile_phone_regex = RegexValidator(
#     regex=r'^\+?1?\d{9,15}$',
#     message=str(
#         'Номер телефона должен быть введен в формате: "+999999999". '
#         'Максимальная длина номера - 15 символов.'
#     )
# )
#
# city_phone_regex = RegexValidator(
#     regex=r'^\2?1?\d{9,6}$',
#     message=str(
#         'Номер городского телефона должен быть введен в формате: "2999999". '
#         'Максимальная длина номера - 7 символов.'
#     )
# )


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
        # validators=[mobile_phone_regex],
        help_text='Номер мобильного телефона',
    )
    city_phone = models.CharField(
        max_length=7,
        # validators=[city_phone_regex],
        help_text='Номер городского телефона',
    )
    hobby = models.TextField()
    skills = models.TextField()
    interests = models.TextField()
    # achievements = ...
    # experience = ...
