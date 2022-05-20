from django.urls import path

from core.views import index, signup, shop
from django.contrib.auth import views

from product.views import product

urlpatterns = [
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path(
        "login/", views.LoginView.as_view(template_name="core/login.html"), name="login"
    ),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("shop/", shop, name="shop"),
    path("shop/<slug:slug>/", product, name="product"),
]
