from django.shortcuts import render

from .models import Product
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

    return render(request, "products/details.html", context)