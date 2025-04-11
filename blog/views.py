from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article



class Index(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/index.html'
    paginate_by = 3

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        article = self.get_object()
        return context