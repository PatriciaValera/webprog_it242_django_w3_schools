from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("<h2>Hello WEBPROG IT242 world!</h2>")