from django.urls import path
from . import views

urlpatterns = [
    path("", views.mfc1_page, name="mfc1_page"),
    path("mfc1_dashboard/", views.mfc1_dashboard, name="mfc1_dashboard")
]
