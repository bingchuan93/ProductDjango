from django.urls import path
from products.views import products_view, product_create_view, product_lookup_view, render_initial_data

app_name = 'products'
urlpatterns = [
    path('', products_view, name='products'),
    # path('', render_initial_data, name='products'),
    path('create/', product_create_view, name='product_create'),
    path('details/<int:id>/', product_lookup_view, name='product_lookup'),
    path('details/<int:id>/', product_lookup_view, name='product_details')
]