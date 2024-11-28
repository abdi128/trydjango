from django.contrib import admin
from articles.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp','user', 'updated', 'publish')
    search_fields = ('id', 'title')
    raw_id_fields = [ 'user' ]


admin.site.register(Article, ArticleAdmin)