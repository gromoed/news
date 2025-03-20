from django.contrib import admin
from .models import NewsArticle


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")
    search_fields = ("title", "author")
    list_filter = ("author", "published_date")


admin.site.register(NewsArticle, NewsArticleAdmin)

