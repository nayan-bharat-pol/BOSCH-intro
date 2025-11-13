"""
URL configuration for bosch_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mfc4 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("bosch_intro.urls")),
    path('mfc/', include("bosch_intro.urls")),  # ✅ link app
    path('mfc4/',include("mfc4.urls")),
    path('mfc4_product/', include("mfc4_product.urls")),
    path('mfc1/', include("mfc1.urls")),
    path('mfc2/', include("mfc2.urls")),
    path('mfc1_product/', include("mfc1_product.urls")),
    path('mfc2_product/', include("mfc2_product.urls")),
    path('c_coating/', views.c_coating),
   ]

