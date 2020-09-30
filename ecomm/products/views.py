from django.shortcuts import render

from products.models import Product

# Create your views here.

def list_products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/list.html', context=context)