from account.forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = SignupForm()

    return render(request, "account/signup.html", {"form": form})


@login_required
def account(request):
    return render(request, "account/account.html")


@login_required
def edit_account(request):
    print("edit_account")
    if request.method == "POST":
        request.user.first_name = request.POST.get("first_name")
        request.user.last_name = request.POST.get("last_name")
        request.user.email = request.POST.get("email")
        request.user.save()
        print("done")
        return redirect("account")

    return render(request, "account/edit_account.html")
