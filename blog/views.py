from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Index(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/index.html'
    paginate_by = 2

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        article = self.get_object()
        if article.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        return context
    
class LikeArticle(View):
    def post(self, request, pk):
        article = Article.objects.get(id=pk)
        if article.likes.filter(pk=self.request.user.id).exists():
            article.likes.remove(request.user.id)
        else:
            article.likes.add(request.user.id)
        article.save()
        return redirect('post_detail', pk)
    
class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('bloglist')
    template_name = 'blog/post_delete.html'

    def test_func(self):
        article = Article.objects.get(id=self.kwargs.get('pk'))
        return self.request.user.id == article.author.id
    
class CreateArticleView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('bloglist')

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    
class UpdateArticleView(UpdateView):
   model = Article
   fields = ['title', 'content']
   template_name = 'blog/post_update.html' 
   def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


    

  
    
