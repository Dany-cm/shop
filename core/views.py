from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import redirect, render
from product.models import Category, Products

from core.forms import SignupForm


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


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = SignupForm()

    return render(request, "core/signup.html", {"form": form})


def login_old(request):
    return render(request, "core/login.html")
