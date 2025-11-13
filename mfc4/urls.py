from django.urls import path
from . import views

urlpatterns = [
    path("", views.mfc4_page, name="mfc4_page"),
    path("mfc4_dashboard/", views.mfc4_dashboard, name="mfc4_dashboard"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("c_coating/", views.c_coating, name="c_coating"),
    path("shopfloor/", views.shopfloor, name="shopfloor"),
]
