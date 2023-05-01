from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User



def loginUser(request):
   context = {}

   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")

      user = authenticate(username=username, password=password)

      if user is not None:
         login(request,user)
         return redirect("indexPage")
      
   return render(request, 'user/login.html', context)

def logoutUser(request):
   logout(request)
   return redirect("indexPage")

def registerUser(request):
   context = {}
   
   if request.method == "POST":
      fname = request.POST.get("fname")
      email = request.POST.get("email")
      username = request.POST.get("username")
      password1 = request.POST.get("password1")
      password2 = request.POST.get("password2")
      
      if password1 == password2:
         if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
               user = User.objects.create_user(username=username, password=password1, first_name=fname, email=email)
               user.save()
               return redirect("loginUser")
   
   return render(request, 'user/register.html', context)



