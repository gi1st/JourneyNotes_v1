from django.urls import path

from accounts.views import(
    registrer_view,
    login_view,
    logout_view,
    change_password_view
)


urlpatterns = [
    path("register/", registrer_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("change-password/", change_password_view, name="change_password"),
]

app_name = "accounts"
