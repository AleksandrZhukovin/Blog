from django.urls import path

from server.apps.blog.logic import *


app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('welcome/', GreetingView.as_view(), name='greeting'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    # Test pages for previewing design
    path('test/article/', ArticleTestView.as_view(), name='article_test'),
]
