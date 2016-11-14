from django.contrib import admin
from Article.models import Article, Comment


class CommentStackInLine(admin.StackedInline):
	model = Comment
	extra = 1


class ArticleAdmin(admin.ModelAdmin):
	fields = ['article_title', 'article_text', 'article_date', ]
	inlines = [CommentStackInLine]
	list_filter = ['article_date',]


admin.site.register(Article, ArticleAdmin)