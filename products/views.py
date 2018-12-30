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
    # form = ProductCreateForm(request.POST or None, instance=obj) #changes database data
    form = ProductCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductCreateForm()

    context = {
        'form': form
    }

    return render(request, "products/product_create.html", context)

def product_lookup_view(request, id):
    obj = Product.objects.get(id=id)
    next_obj= Product.objects.filter(id__gt=obj.id).order_by('id').first()
    prev_obj= Product.objects.filter(id__lt=obj.id).order_by('id').first()
    context = {
        'object' : obj,
        'prev_product_id' : prev_obj.id if prev_obj else 1,
        'next_product_id' : next_obj.id if next_obj else obj.id
    }
    return render(request, "products/product_lookup.html", context)

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