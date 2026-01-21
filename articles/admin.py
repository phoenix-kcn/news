from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin): 
    list_display = ('title', 'author', 'date')
    # search_fields = ('title', 'body', 'author__username')
    # list_filter = ('date', 'author')

admin.site.register(Article, ArticleAdmin)