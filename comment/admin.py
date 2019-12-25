from django.contrib import admin

from .models import Comment
# Register your models here.


@admin.register(Comment)
class CommentModel(admin.ModelAdmin):
    """配置评论后台管理"""
    list_display = ['target', 'nickname', 'content', 'website', 'created_time']
