from django.shortcuts import render
from django.urls import path     # ✅ Add this import
from . import views              # ✅ Keep your views import


urlpatterns = [
    path("", views.mfc1_product, name="mfc1_product"),
]
