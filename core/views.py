from django.db.models import Q
from django.shortcuts import render
from product.models import Category, Products


def index(request):
    return render(request, "core/index.html", {"products": Products.objects.all()[0:8]})


def shop(request):
    categories = Category.objects.all()
    products = Products.objects.all()

    # Filter products by category
    if active_category := request.GET.get("category"):
        products = products.filter(category__slug=active_category)

    # Filter products by search
    if query := request.GET.get("query"):
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    context = {
        "categories": categories,
        "products": products,
        "active_category": active_category,
    }
    return render(request, "core/shop.html", context)
