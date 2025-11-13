from django.urls import path
from . import views

urlpatterns = [
    path("", views.mfc4_product, name="mfc4_product"),
    path("valve_piece/", views.valve_piece, name="valve_piece"),
    path("valve_piston/", views.valve_piston, name="valve_piston"),
    path("Armature_bolt/", views.Armature_bolt, name="Armature_bolt"),
    path("Armature_plate/", views.Armature_plate, name="Armature_plate"),
    path("Armature_guide/", views.Armature_guide, name="Armature_guide"),
    path("product/", views.mfc4_product, name="mfc4_product"),    
]
