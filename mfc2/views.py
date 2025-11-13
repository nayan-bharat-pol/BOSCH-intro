from django.shortcuts import render

def mfc2_page(request):
    return render(request, "mfc2/mfc2_page.html")

def dashboard2(request):
    return render(request, "mfc2/dashboard2.html")