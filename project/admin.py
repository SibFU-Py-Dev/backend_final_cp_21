from django.contrib import admin

from project.models import *


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization')
    list_display_links = ('name', 'specialization')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )


class AccessRequestInline(admin.StackedInline):
    model = AccessRequest


class ArticleFileInline(admin.StackedInline):
    model = ArticleFile


class HintInline(admin.StackedInline):
    model = Hint
    fk_name = 'target'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    inlines = [
        AccessRequestInline,
        ArticleFileInline,
        HintInline
    ]
