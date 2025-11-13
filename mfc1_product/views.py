from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def mfc1_product(request):
    return render(request, "mfc1_product/mfc1.html")