from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    context = {}
    return render(request, "home.html", context)

def contact_view(request, *args, **kwargs):
    context = {}
    return render(request, "contact.html", context)

def about_view(request, *args, **kwargs):
    context = {
        'title': 'About Page',
        'phone_number': 91000480,
        'hobbies': ['Cards', 'Skates', 'Guitar']
    }
    return render(request, "about.html", context)

def products_view(request, *args, **kwargs):
    context = {}
    return render(request, "products.html", context)