from django.shortcuts import render
from django.http import HttpResponse

def about_us(request):
    """Created the html request that will be triggered when this about_us page is called"""
    return render(request, "about_us.html")
