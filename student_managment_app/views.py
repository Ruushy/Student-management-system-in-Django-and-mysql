from django.shortcuts import render , HttpResponse , HttpResponseRedirect
from student_managment_app.EmailBackEnd import EmailBackend
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from django.urls import reverse
from .models import CustomerUser
# Create your views here.

def DemoPage(request):
    return render(request, "demo.html")

def ShowloginPage(request):
    return render(request, "login_page.html")

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>method not Allowded</h2>")
    else :
        user=EmailBackend.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user != None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("stuff_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
                
                   
               
        else:
            messages.error(request, "invalid login")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+"user type"+request.user.user_type)
    
def Logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")