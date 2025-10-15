from django.db import models

from server.apps.core.models import TimeStampedModel


class Article(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.TextField()


class ArticleImage(TimeStampedModel):
    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE, related_name='images')

    image = models.ImageField(upload_to='images/articles/')
