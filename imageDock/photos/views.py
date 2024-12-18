from django.shortcuts import render,redirect
from .models import Category,Photo
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def gallery(request):

    category=request.GET.get('category')

    if(category == None):
        photo=Photo.objects.all()
    else:

        photo=Photo.objects.filter(category__name=category)
    

    categories = Category.objects.all()
    
    context = {'categories' : categories,'photos':photo}
    return render(request,"photos/gallery.html",context)

def deletePhoto(request,pk):
    photo= Photo.objects.get(id=pk)
    photo.delete()
    return HttpResponseRedirect(reverse('gallery'))

def viewPhoto(request,pk):
    photo= Photo.objects.get(id=pk)
    return render(request,"photos/photo.html",{'photo':photo})

def addPhoto(request):
     categories = Category.objects.all()
     if request.method == 'POST':
        data=request.POST
        image=request.FILES.get("image")

        if data["category"] != "none":
            category = Category.objects.get(id=data["category"])
        elif(data["category_new"]!=''):
            category,created= Category.objects.get_or_create(name=data["category_new"])
        else:
            category=None


        photo=Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )

        return redirect("gallery")


     context = {'categories' : categories}
     return render(request,"photos/add.html",context)