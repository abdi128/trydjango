from django.contrib import admin
from articles.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp','slug', 'updated', 'publish')
    search_fields = ('id', 'title')


admin.site.register(Article, ArticleAdmin)