from django.shortcuts import render

def index(request):
    return render(request, "bosch_intro/index.html")