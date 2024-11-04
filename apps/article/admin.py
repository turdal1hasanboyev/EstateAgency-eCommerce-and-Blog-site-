from django.contrib import admin
from .models import Article, ArticleCategory, ArticleTag, Comment


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at', 'updated_at')
    ordering = ('id',)
    search_fields = ('name',)
    list_filter = ('is_active',)
    prepopulated_fields = {
        'slug': ('name',)
    }
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    search_fields = ('name',)
    list_filter = ('is_active',)
    prepopulated_fields = {
        'slug': ('name',)
    }
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sub_title', 'category', 'author', 'views', 'is_active', 'created_at', 'updated_at')
    ordering = ('title',)
    search_fields = ('title', 'sub_title', 'category__name', 'author__email',)
    prepopulated_fields = {
        'slug': ('title',)
    }
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'category',
        'author',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'user', 'name', 'email', 'web_site', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    search_fields = ('name', 'email', 'article__title', 'user__email', 'web_site')
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'is_active',
        'article',
        'user',
    )