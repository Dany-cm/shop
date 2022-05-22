from django.urls import path

from cart.views import cart, add_to_cart, checkout, hx_cart_menu, hx_cart_total, update_cart, success


urlpatterns = [
    path("", cart, name="cart"),
    path("success/", success, name="success"),
    path("checkout", checkout, name="checkout"),
    path("add_to_cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path('update_cart/<int:product_id>/<str:action>/', update_cart, name='update_cart'),
    path("hx_cart_menu/", hx_cart_menu, name="hx_cart_menu"),
    path("hx_cart_total/", hx_cart_total, name="hx_cart_total"),
]
