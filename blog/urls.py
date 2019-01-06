from django.urls import path
from blog.views import (
    article_details,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
)

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:id>/details', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:id>/update', ArticleUpdateView.as_view(), name='article_update'),
    path('details/', article_details, name='article_details')
]