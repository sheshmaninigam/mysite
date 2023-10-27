from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from users.forms import SignUpForms
from django.contrib.auth.decorators import login_required



# Create your views here.



def signup(request):
  if request.method =="POST":
    form = SignUpForms(request.POST)

    if form.is_valid():
      username = form.cleaned_data.get("username")
      messages.success(
        request,
        f"welcome {username}, you have been Successfully Signup"
      )
      form.save()
      return redirect ("login")
    
  else:
      form = SignUpForms()
      context ={
        "form": form
      }
      
      return render(request, "users/signup.html",context)
   

 

def login_view(request):
    
    if request.method == 'POST':
       username = request.POST["username"]
       password = request.POST["password"]
       user = authenticate(request, username=username, password=password)
       
       if user is None:
        messages.success(
           request,
           "Invalid login"
        )
        return redirect("login")

       elif user.is_superuser:
        login(request,user)
        messages.success(
            request,
            f"Welcome Superuser {request.user.username},you have been Successfully login"
        )
        return redirect("car:index")

       elif user is not None:
        login(request,user)
        messages.success(
            request,
            f"Welcome {request.user.username},you have been Successfully login"
        )
        return redirect("car:index")

    return render(request, "users/login.html")


def logout_view(request):
   messages.success(
      request,
      f"{request.user.username}, you have been Successfully logout"
   )
   logout(request)
   return redirect("car:index")

@login_required
def profile_views(request):
   return render(request, "users/profile.html")
