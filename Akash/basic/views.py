from django.http import HttpResponse
from django.shortcuts import redirect, render

from . import models
from . import forms

# Create your views here.

def callRead(req,which):
    obj=models.Game.objects.get(id=which)
    return render(req,"read.html",{"single":obj})

def callList(req):
    obj=models.Game.objects.all()
    return render(req,"list.html",{"mylist":obj})


def callCreateOrEdit(req,theone=0):
    if req.method=="POST":
        if theone!=0:# update
            ex=models.Game.objects.get(id=theone)
            print(ex.name+" old")
        else:
            object=forms.GameForm(req.POST)
        if object.is_valid():
            object.save()
            return redirect('/giri/');
        else:
            return render(req,"create.html",{"hey":object,"info":"New game not added"})
    else:
        if theone!=0:
            obj=models.Game.objects.get(id=theone)
            exist=forms.GameForm(instance=obj)
            return render(req,"create.html",{"hey":exist,"title":"Update existing game"})
        else:
            obj=forms.GameForm()
            return render(req,"create.html",{"hey":obj,"title":"New game creation"})
    # for save alone
    # if req.method=="POST":
    #     object=forms.GameForm(req.POST)
    #     if object.is_valid():
    #         object.save()    
    #         #return render("/giri/new")
    #         obj=forms.GameForm()
    #         #return render(req,"create.html",{"hey":obj,"info":"New game added"})
    #         return redirect('/giri/');
    #     else:
    #         return render(req,"create.html",{"hey":object,"info":"New game not added"})
    # else:
    #     obj=forms.GameForm()
    #     return render(req,"create.html",{"hey":obj,"info":"New game"})

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