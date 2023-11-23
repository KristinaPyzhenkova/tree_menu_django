from django.contrib import admin
from app import models


@admin.register(models.MenuItem)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'url',
        'parent',
    )
    search_fields = ('title',)
    empty_value_display = '-пусто-'
    ordering = ('-id',)
