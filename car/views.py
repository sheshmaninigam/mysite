from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "car/index.html")
    # return HttpResponse("This is my home page")


def about(request):
    return HttpResponse("This is my about page")

def services(request):
    return HttpResponse("This is my services page")

def contact(request):
    return HttpResponse("This is my contact page")

