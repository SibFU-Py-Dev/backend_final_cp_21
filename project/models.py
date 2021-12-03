from re import template
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


phone_regex = RegexValidator(
    regex = r'^\+?1?\d{9,15}$',
    message = str(
        'Номер телефона должен быть введен в формате: "+999999999". '
        'Максимальная длина номера - 15 символов.'
    )
)

# Create your models here.
class Member(models.Model):
    name = models.CharField(
        max_length=40,
        help_text='ФИО участника команды',
    )
    specialization = models.CharField(
        max_length=40,
        help_text='Компетенция участника команды',
    )
    telegram = models.CharField(
        max_length=40,
        help_text='Контакты участника в телеграм',
    )
    mail = models.EmailField(
        max_length=40,
        help_text='Почта участника',
    )
    phone = models.CharField(
        max_length=17,
        validators=[phone_regex],
        help_text='Номер телефона участника',
    )
    project = models.ForeignKey(
        to='Project',
        related_name='members',
        related_query_name='member',
        on_delete=models.CASCADE,
        null=True,
        help_text='Проект участника команды',
    )


class Resource(models.Model):

    class ResourceType(models.TextChoices):
        GITHUB = 'GH', _('GitHub')
        GITLAB = 'GL', _('GitLab')
        JIRA = 'JR', _('Jira')
        CONFLUENCE = 'CF', _('Confluence')
        WIKI = 'WK', _('Wiki')
        OTHER = 'TH', _('Other')

    name = models.CharField(
        max_length=40,
        help_text='Название ресурса проекта',
    )
    project = models.ForeignKey(
        to='Project',
        related_name='resources',
        related_query_name='resource',
        on_delete=models.SET_NULL,
        null=True,
        help_text='Проект этого ресурса',
    )
    link = models.URLField(
        max_length=100,
        help_text='Ссылка на проектный ресурс',
    )
    type = models.CharField(
        max_length=2,
        choices=ResourceType.choices,
        default=ResourceType.OTHER,
        help_text='Тип ресурса проекта',
    )


class AccessRequest(models.Model):
    resource = models.OneToOneField(
        to='Resource',
        related_name='access',
        related_query_name='access',
        on_delete=models.CASCADE,
        help_text='Ресурс проекта',
    )
    link = models.URLField(
        max_length=100,
        help_text='Ссылка на ресурс в IDM',
    )
    template_content = models.TextField(
        help_text='Заготовка заявки на получение доступа',
    )


class Project(models.Model):
    title = models.CharField(
        max_length=100,
        help_text='Название проекта',
    )
    purpose = models.TextField(
        help_text='Цель(-ли) проекта',
    )
    issue = models.TextField(
        help_text='Задача(-и) проекта',
    )
    managment_info = models.TextField(
        help_text='Обязательные мероприятия по скраму',
    )
    calendar_info = models.TextField(
        help_text='План работ и контрольные точки',
    )
    result_info = models.TextField(
        help_text='Результаты проекта',
    )
