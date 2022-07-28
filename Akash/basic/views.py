from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


    

def logging(req):
    if req.method=="POST":
        u=req.POST['username']
        p=req.POST['passw']
        
        if u=='akash' and p=='tamilgiri':
            return render(req,"yet.html")
        else:
            return render(req,"login.html",{"info":"invalid credentials"})
    else:
        return render(req,"login.html")

'''def getting(req):
    if req.method=="POST":
        u=req.POST['username']
        p=req.POST['passw']
        
        if u=='akash' and p=='tamilgiri':
            return render(req,"yet.html")
        else:
            return render(req,"login.html",{"info":"invalid credentials"})
    

def logging(req):
    return render(req,"login.html")'''

def show(req):
    return render(req,"yet.html")

def hello(request):
    return HttpResponse("<h1>Welcome to Zealous Tech Corp</h1>")

def haiThere(req):
    return HttpResponse("<ul type='square'><li>HTML</li><li>Jinja</li></ul>")