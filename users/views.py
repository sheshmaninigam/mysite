from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from users.forms import SignUpForms
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from users.forms import ProfileForm



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

@login_required(login_url="login")
def profile_views(request):
   return render(request, "users/profile.html")

def profile_edit(request,id):
  profile = Profile.objects.get(pk=id)
  form = ProfileForm(request.POST or None, request.FILES, instance=profile)

  if form.is_valid():
    form.save()
    messages.success(
      request,
      f"Your profile {request.user.username}, is Successfully Change"
    )
    return redirect("car:index")
  
  else:
        form = ProfileForm(instance=profile)
  
  context = {
    "form":form
  }


  return render(request,"users/profile_edit.html",context)


# class ProfileUpdateView(UpdateView):
#   model = Profile
#   template_name = 'users/profile_edit.html'
#   fields = ['image','location']
#   success_url = reverse_lazy('users:profile')