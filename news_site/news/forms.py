from django import forms
from news_site.news.models import NewsArticle


class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ["title", "content", "author", "published_date", "categories"]
        widgets = {
            "categories": forms.CheckboxSelectMultiple()
        }

