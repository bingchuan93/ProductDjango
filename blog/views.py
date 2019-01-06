from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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

class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    queryset = Blog.objects.all()               #not needed. but filters the data before returning selecting/filtering

    def get_object(self):
        id_ = self.kwargs.get("id")             #self.kwargs are passed in from the url
        return get_object_or_404(Blog, id=id_)

class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Blog.objects.all()
    # success_url = '/blog'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    #def get_success_url(self):
    #    return '/blog'

class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Blog.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Blog, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

def article_details(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ArticleForm()

    context = {
        'form': form
    }
    return render(request, "blog/article_details.html", context)