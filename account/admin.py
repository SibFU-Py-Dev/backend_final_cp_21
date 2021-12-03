from django.contrib import admin

from account.models import *


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', )
