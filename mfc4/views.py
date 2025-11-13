from django.shortcuts import render

def mfc4_page(request):
    return render(request, "mfc4/mfc4_page.html")

def product(request):
    return render(request, "mfc4/product.html")

def mfc4_dashboard(request):
    return render(request, "mfc4/mfc4_dashboard.html")

def c_coating(request):
    return render(request, "c_coating/coating.html")

def shopfloor(request):
    return render(request, "mfc4/shopfloor.html")

def dashboard(request):
    return render(request, "c_coating/dashboard.html")
    