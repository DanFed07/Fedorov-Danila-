from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import News, Article, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'is_main']
    list_filter = ['published_date', 'is_main']
    search_fields = ['title', 'content']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date', 'views_count']
    list_filter = ['created_date']
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'get_target', 'created_date', 'is_approved']
    list_filter = ['is_approved', 'created_date']

    def get_target(self, obj):
        if obj.news:
            return f"Новость: {obj.news.title}"
        return f"Статья: {obj.article.title}"

    get_target.short_description = 'Цель'