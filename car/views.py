from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    
    context={
        "variable":"1"
    }
    return render(request, "car/index.html",context)
    # return HttpResponse("This is my home page")


def about(request):
    return render(request, "car/about.html")

def Add_car(request):
    return render(request,"car/add-car.html")

def contact(request):
    return render(request,"car/contact.html")

