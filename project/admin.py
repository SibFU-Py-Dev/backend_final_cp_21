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


@admin.register(AccessRequest)
class AccessRequestAdmin(admin.ModelAdmin):
    list_display = ('link', )
    list_display_links = ('link', )


class ArticleFileInline(admin.StackedInline):
    model = ArticleFile


@admin.register(Hint)
class HintAdmin(admin.ModelAdmin):
    list_display = ('source', 'target')
    list_display_links = ('source', 'target')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    inlines = [
        ArticleFileInline,
    ]
