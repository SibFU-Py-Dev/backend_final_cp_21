from re import template
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _


phone_regex = RegexValidator(
    regex = r'^\+?1?\d{9,15}$',
    message = str(
        'Номер телефона должен быть введен в формате: "+999999999". '
        'Максимальная длина номера - 15 символов.'
    )
)


def article_directory_path(instance, filename):
    # Загрузка файлов в MEDIA_ROOT/article_<id>/<filename>
    return 'article_{0}/{1}'.format(instance.article.id, filename)

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
        blank=True,
        help_text='Проект участника команды',
    )


class Article(models.Model):
    title = models.CharField(
        max_length=40,
        help_text='Название статьи проекта',
    )
    content = models.TextField(
        help_text='Описание статьи'
    )
    resource_link = models.URLField(
        max_length=100,
        null=True,
        help_text='Ссылка на ресурс статьи',
    )
    resource_link_1 = models.URLField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Ссылка на ресурс статьи',
    )
    resource_link_2 = models.URLField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Ссылка на ресурс статьи',
    )
    video_link = models.TextField(
        max_length=100,
        null=True,
        help_text='Ссылка на видео-описание ресурса',
    )
    prev = models.ForeignKey(
        'self',
        on_delete=SET_NULL,
        related_name='nextful',
        null=True,
        blank=True,
        help_text='Предыдущая статья в списке',
    )
    next = models.ForeignKey(
        'self',
        on_delete=SET_NULL,
        related_name='prevful',
        null=True,
        blank=True,
        help_text='Следующая статья в списке',
    )
    project = models.ForeignKey(
        to='Project',
        related_name='articles',
        related_query_name='article',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Проект, в котором содержится эта статья',
    )

    # def get_json(self):
    #     return {
    #         "title": self.title,
    #         "content": self.content,
    #         "resource_link": self.resource_link,
    #         "video_link": self.video_link,
    #         "prev": self.prev,
    #         "next": self.next,
    #         "files": [f.file for f in ArticleFile.objects.filter(pk=self.pk)],
    #         "project": self.project,
    #     }


class Hint(models.Model):
    source = models.ForeignKey(
        'Article',
        related_name='source_hints',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    target = models.OneToOneField(
        'Article',
        related_name='target_hint',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=50,
        help_text='Название ресурса под ссылку',
    )
    comment = models.CharField(
        max_length=100,
        blank=True,
        help_text='Комментарий к связке статей',
    )


class ArticleFile(models.Model):
    file = models.FileField(
        upload_to=article_directory_path,
        help_text='',
    )
    article = models.ForeignKey(
        to='Article',
        related_name='files',
        related_query_name='file',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='Файлы конкретной статьи',
    )


class AccessRequest(models.Model):
    link = models.URLField(
        max_length=100,
        help_text='Ссылка на ресурс в IDM',
    )
    template_content = models.TextField(
        help_text='Заготовка заявки на получение доступа',
    )
    article = models.OneToOneField(
        to='Article',
        related_name='access',
        related_query_name='access',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='Ресурс проекта',
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
