from django.db import models


class Survey(models.Model):
    title = models.TextField(verbose_name='Заголовок опроса')


class Question(models.Model):
    title = models.TextField(verbose_name='Вопрос')
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
    )
    description = models.TextField(verbose_name='Хочу написать подробнее')


class AnswerOption(models.Model):
    answer = models.TextField(verbose_name='Ответ')
