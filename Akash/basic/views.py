from django.http import HttpResponse
from django.views.decorators.cache import cache_control
from django.shortcuts import get_object_or_404, redirect, render

from . import models
from . import forms

# Create your views here.

def callOut(req):
    if req.session.has_key('authoriser'):
        req.session['authoriser']=""
        del req.session['authoriser']
        return redirect("/giri/")
    else:
        return render(req,'login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True,expires=0)
def callShort(req):
    if req.session.has_key('authoriser'):
        if req.method=="POST":
            data=[]
            yr=req.POST['year']
            dv=req.POST['device']
            pl=req.POST['player']
            if yr!="" and dv=="" and pl=="":
                print("BAsed on released year")
                yr=int(yr)
                data=models.Game.objects.filter(year__gte=yr)
            elif yr=="" and dv!="" and pl=="":
                print("BAsed on device")
                data=models.Game.objects.filter(device__icontains=dv)
            elif yr=="" and dv=="" and pl!="":
                print("BAsed on player")
                data=models.Game.objects.filter(topplayer__icontains=pl)
            else:
                print("invalid")
            return render(req,"list.html",{"mylist":data})
        else:
            return render(req,"shortlist.html")
    else:
        return render(req,'login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True,expires=0)
def callDelete(req,key):
    if req.session.has_key('authoriser'):
        obj=get_object_or_404(models.Game,id=key)
        models.Game.delete(obj)
        return redirect("/giri/home")
    else:
        return render(req,'login.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True,expires=0)
def callEdit(request,theone):
    if request.session.has_key('authoriser'):
        if request.method=="POST":
            #new way
            #obj=get_object_or_404(models.Game,id=theone)
            #exist=forms.GameForm(request.POST or None,instance=obj)
            
            #old way
            obj=models.Game.objects.get(id=theone)
            exist=forms.GameForm(request.POST,instance=obj)
            if exist.is_valid():
                exist.save()
                return redirect('/giri/home');
        else:
            #new way
            #obj=get_object_or_404(models.Game,id=theone)
            #exist=forms.GameForm(instance=obj)
            
            #old way
            obj=models.Game.objects.get(id=theone)
            exist=forms.GameForm(instance=obj)
            return render(request,"edit.html",{"hey":exist,"title":"Update existing game"})
    else:
        return render(request,'login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True,expires=0)   
def callRead(req,which):
    if req.session.has_key('authoriser'):
        obj=models.Game.objects.get(id=which)
        return render(req,"read.html",{"single":obj})
    else:
        return render(req,'login.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True,expires=0)
def callList(req):
    if req.session.has_key('authoriser'):
        obj=models.Game.objects.all()
        return render(req,"list.html",{"mylist":obj})
    else:
        return render(req,'login.html')


# def callCreateOrEdit(req,theone=0):
#     if req.method=="POST":
#         print(theone)
#         if theone!=0:# update
#             ex=models.Game.objects.get(id=theone)
#             print(ex.name,ex.id,ex.device)
#             obj=forms.GameForm(req.POST or None,instance=ex)
#             if obj.is_valid():
#                 obj.save()
#                 return redirect('/giri/');
#         else:
#             object=forms.GameForm(req.POST)
#         # else:
#         #     return render(req,"create.html",{"hey":object,"info":"New game not added"})
#         return redirect("/giri/")
#     else:
#         if theone!=0:
#             obj=models.Game.objects.get(id=theone)
#             exist=forms.GameForm(instance=obj)
#             return render(req,"create.html",{"hey":exist,"title":"Update existing game"})
#         else:
#             obj=forms.GameForm()
#             return render(req,"create.html",{"hey":obj,"title":"New game creation"})


    # for save alone
@cache_control(no_cache=True,must_revalidate=True,no_store=True,expires=0)
def callCreate(req):
    if req.session.has_key('authoriser'):
        if req.method=="POST":
            object=forms.GameForm(req.POST)
            if object.is_valid():
                object.save()    
                #return render("/giri/new")
                obj=forms.GameForm()
                #return render(req,"create.html",{"hey":obj,"info":"New game added"})
                return redirect('/giri/home')
        else:
            obj=forms.GameForm()
            return render(req,"create.html",{"hey":obj,"title":"New game creation"})
    else:
        return render(req,"login.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True,expires=0)
def logging(req):
    if req.method=="POST":
        u=req.POST['username']
        p=req.POST['passw']
        if u=='akash' and p=='tamilgiri':
            req.session['authoriser']=u
            return render(req,"home.html")
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