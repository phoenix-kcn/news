from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content', 'author']
    template_name = 'article_form.html'
    success_url = '/articles/'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = '/articles/'