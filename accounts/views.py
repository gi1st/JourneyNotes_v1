from django.shortcuts import render, redirect
from django.contrib.auth import login

from accounts.forms import RegisterForm


def registrer_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("journeys:journeys_list")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    pass


def logout_view(request):
    pass


def change_password_view(request):
    pass
