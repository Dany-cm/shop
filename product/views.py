from django.shortcuts import get_object_or_404, render

from product.models import Products

# Create your views here.


def product(request, slug):
    product = get_object_or_404(Products, slug=slug)

    return render(request, "product/product.html", {"product": product})
