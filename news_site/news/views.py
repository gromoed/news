from django.shortcuts import render, redirect
from .models import NewsArticle
from .forms import NewsArticleForm

def news_list(request):
    articles = NewsArticle.objects.all()
    return render(request, "./news_list.html", {"articles": articles})


def add_news(request):
    if request.method == "POST":
        form = NewsArticleForm(request.POST)
        if form.is_valid():
            news_article = form.save()
            return redirect("news_list")
        else:
            form = NewsArticleForm

        return render(request, "news/add_news.html", {"form": form})
