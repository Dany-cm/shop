from django.urls import path

from dashboard.views import dashboard, product, add_product, delete_product, edit_product, delete_product, order, edit_order

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("product/", product, name="product"),
    path("add_product/", add_product, name="add_product"),
    path("edit_product/<int:product_id>/", edit_product, name="edit_product"),
    path("delete_product/<int:product_id>/", delete_product, name="delete_product"),
    path("order/", order, name="order"),
    path("edit_order/<int:order_id>/", edit_order, name="edit_order"),
]
