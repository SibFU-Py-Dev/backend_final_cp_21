from django.contrib import admin

from tests.models import *


class AnswerOptionInline(admin.StackedInline):
    model = AnswerOption


@admin.register(Question)
class QuestionInline(admin.ModelAdmin):
    list_display = ('title', )
    inlines = [
        AnswerOptionInline,
    ]


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', )
