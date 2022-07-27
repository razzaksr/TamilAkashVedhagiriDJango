from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def show(req):
    return render(req,"yet.html")

def hello(request):
    return HttpResponse("<h1>Welcome to Zealous Tech Corp</h1>")

def haiThere(req):
    return HttpResponse("<ul type='square'><li>HTML</li><li>Jinja</li></ul>")