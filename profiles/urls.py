from django.urls import path

from . import views

app_name = "profiles"

urlpatterns = [
    path("account/", views.account_settings, name="account_settings"),  # <-- this must come first!
    path("<str:username>/", views.ProfileDetailView.as_view(), name="detail"),
]
