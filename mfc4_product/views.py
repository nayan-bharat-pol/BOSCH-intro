from django.shortcuts import render

def mfc4_product(request):
    return render(request, "mfc4_product/mfc4_product.html")

def valve_piece(request):
    return render(request, "mfc4_product/valve_piece.html")

def valve_piston(request):
    return render(request, "mfc4_product/valve_piston.html")

def Armature_bolt(request):
    return render(request, "mfc4_product/Armature_bolt.html")

def Armature_plate(request):
    return render(request, "mfc4_product/Armature_plate.html")

def Armature_guide(request):
    return render(request, "mfc4_product/Armature_guide.html") 