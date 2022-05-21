from django.urls import path
from product.views import product

from core.views import index, shop

urlpatterns = [
    path("", index, name="index"),
    path("shop/", shop, name="shop"),
    path("shop/<slug:slug>/", product, name="product"),
]
