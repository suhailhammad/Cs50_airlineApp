from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
  if not request.user.is_authenticated: #request has user object, whech has is_authenticated method within
    return HttpResponseRedirect(reverse("login"))
  return render(request, "users/user.html")


def login_view(request):
  if request.method=="POST":
    username = request.POST["username"]  # save username in a variable
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password) # authenticate is a system function takes username and password which we imported above
    if user is not None: #means authenticatio process is OK
      login(request, user)  # login is a system function also
      return HttpResponseRedirect(reverse("index"))
    else:
      return render(request, "users/login.html", {
        "message"   : "invalid credentials."
      })
  return render(request, "users/login.html")

def logout_view(request):
  logout(request)
  return render(request, "users/login.html", {
    "message"   : "logged out."
  })
