from account.views import account, edit_account, signup
from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    path("signup/", signup, name="signup"),
    path(
        "login/", views.LoginView.as_view(template_name="account/login.html"), name="login"
    ),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("", account, name="account"),
    path("edit/", edit_account, name="edit_account"),
]
