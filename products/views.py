from django.shortcuts import render

from .models import Product
from .forms import ProductCreateForm, RawProductForm
# Create your views here.
def products_view(request, *args, **kwargs):
    context = {}
    return render(request, "products.html", context)

def product_details_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    #     'summary': obj.summary,
    #     'featured': obj.featured
    # }

    context = {
        'product': obj
    }

    return render(request, "products/product_details.html", context)

def product_create_view(request): #Using built in django 'automated' forms
    initial_data = {
        'title': "This is an initial product name"
    }
    obj = Product.objects.get(id=1)
    form = ProductCreateForm(request.POST or None, instance=obj) #changes database data

    if form.is_valid():
        form.save()
        form = ProductCreateForm()

    context = {
        'form': form
    }

    return render(request, "products/product_create.html", context)

# def product_create_view(request):   #raw HTML Form Example
#     print(request.GET)
#     print(request.POST)
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         print(title)
#     context = {
#     }

#     return render(request, "products/product_create.html", context)

# def product_create_view(request):   #pure HTML Form Example
#     form = RawProductForm()
#     if request.method == 'POST':
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         'form': form
#     }

#     return render(request, "products/product_create.html", context)