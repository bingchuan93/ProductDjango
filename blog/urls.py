from django.urls import path
from blog.views import article_details, ArticleListView

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('details/', article_details, name='article_details')
]