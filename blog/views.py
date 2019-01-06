from django.shortcuts import render

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .forms import ArticleForm
from .models import Blog
# Create your views here.

class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Blog.objects.all()

def article_details(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ArticleForm()

    context = {
        'form': form
    }
    return render(request, "blog/article_details.html", context)