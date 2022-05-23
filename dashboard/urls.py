from django.urls import path

from dashboard.views import dashboard, product, add_product, delete_product, edit_product, delete_product

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("product/", product, name="product"),
    path("add_product/", add_product, name="add_product"),
    path("edit_product/<int:product_id>/", edit_product, name="edit_product"),
    path("delete_product/<int:product_id>/", delete_product, name="delete_product"),
]
