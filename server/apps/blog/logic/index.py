from django.views.generic import TemplateView, ListView, DetailView

from server.apps.blog.models import Article


__all__ = (
    'GreetingView',
    'IndexView',
    'ArticleDetailView',
    'ArticleTestView',
)


class GreetingView(TemplateView):
    template_name = 'blog/greeting.html'


class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    ordering = ['-created_at']


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'


class ArticleTestView(TemplateView):
    """Test view to preview article page design without database content."""
    template_name = 'blog/article_test.html'
