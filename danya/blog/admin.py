from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


# Регистрируем модель Пост через Дикоратор
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'create_at', 'id']
    # Перенесли кнопки с нижней части в веерхнюю в админке
    save_as = True
    save_on_top = True


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'create_at', 'id']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)