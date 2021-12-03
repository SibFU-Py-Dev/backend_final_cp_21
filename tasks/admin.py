from django.contrib import admin

from tasks.models import *


class UserTaskInline(admin.StackedInline):
    model = UserTask


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )
    inlines = [
        UserTaskInline,
    ]
