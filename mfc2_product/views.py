from django.shortcuts import render

# Create your views here.


def mfc2_product(request):
    return render(request, "mfc2_product/mfc2.html")