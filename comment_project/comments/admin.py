from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    search_fields = ('title', 'content', 'author__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'date_posted')
    search_fields = ('content', 'user__username', 'post__title')