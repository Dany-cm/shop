from django.urls import path
from product.views import product

from core.views import index, shop, tracking_order

urlpatterns = [
    path("", index, name="index"),
    path("tracking_order", tracking_order, name="tracking_order"),
    path("shop/", shop, name="shop"),
    path("shop/<slug:slug>/", product, name="product"),
]
