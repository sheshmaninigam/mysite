from django.shortcuts import render, HttpResponse
from car.models import Contact

# Create your views here.

def index(request):
    
    context={
        "variable":"1"
    }
    return render(request, "car/index.html",context)
    # return HttpResponse("This is my home page")


def about(request):
    return render(request, "car/about.html",)

def Add_car(request):
    return render(request,"car/add-car.html")

def contact(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request,"car/contact.html")

