from django.shortcuts import render
from django.urls import path     # ✅ Add this import
from . import views              # ✅ Keep your views import


urlpatterns = [
    path("", views.mfc2_product, name="mfc2_product"),
]