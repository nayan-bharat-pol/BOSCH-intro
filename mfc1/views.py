from django.shortcuts import render

def mfc1_page(request):
    return render(request, "mfc1/mfc1_page.html")
 
def mfc1_dashboard(request):
    return render(request, "mfc1/mfc1_dashboard.html")

# def mfc1_page(request):
#     menu_items = "Product Overview,Shopfloor,Dashboard,Connectivity,Awards & Achievements,dddddddd".split(',')
#     return render(request, "mfc1.html", {"menu_items": menu_items})
