from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category, related_name="articles", default=None)

    def __str__(self):
        return self.title