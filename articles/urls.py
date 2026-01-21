from django.urls import path
from .views import ( 
    ArticleListView, 
    ArticleDetailView, # new 
    ArticleUpdateView, # new 
    ArticleDeleteView, # new
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
]
