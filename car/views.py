from django.shortcuts import render, redirect
from car.models import Contact
from car.models import Addcar
from car.forms import Addcar_Form
from django.contrib import messages

# Create your views here.

def index(request):
    Addlist = Addcar.objects.all()
    context={
        "Addlist":Addlist
    }
    return render(request, "car/index.html",context)

def detail_c(request,car_id):

    car = Addcar.objects.get(pk = car_id)

    context ={
        "car":car
    }
    return render(request,"car/detail.html",context)

def about(request):
    return render(request, "car/about.html",)

def Add_car(request):
    form = Addcar_Form(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("car:index")

    context={
        "form":form
    }
    return render(request,"car/add_car.html",context)



def contact(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(
            request,
            "Your message has been Sent"
        )
    return render(request,"car/contact.html")


def search_views(request):
    if request.method == "GET":
        searchfor= request.GET.get("search")
        search = Addcar.objects.filter(car_name__contains=searchfor)

        # search = Addcar.objects.all()
        
        context = {
           "search":search
        }
       
    return render(request,"car/searchbar.html",context)




