from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Comment, News, Token, User

admin.site.register(User, UserAdmin)
admin.site.register(Token)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'text',
                    'date',
                    )
    search_fields = ('title',)
    empty_value_display = '-empty-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'author', 'date')
    search_fields = ('author',)
    empty_value_display = '-empty-'
