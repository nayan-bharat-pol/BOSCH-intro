from django.urls import path
from . import views

urlpatterns = [
    path("", views.mfc2_page, name="mfc2_page.html"),
    path("dashboard2/", views.dashboard2, name="dashboard2")
]
