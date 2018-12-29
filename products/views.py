from django.shortcuts import render

from .models import Product
from .forms import ProductCreateForm
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

# def product_create_view(request):
#     form = ProductCreateForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         form = ProductCreateForm()

#     context = {
#         'form': form
#     }

#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    print(request.GET)
    print(request.POST)
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
    context = {
    }

    return render(request, "products/product_create.html", context)