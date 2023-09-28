from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail

def SignUp(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if(pass1!=pass2):
            return HttpResponse("Password not matched with Confirm Password")
        my_User = User.objects.create_user(uname,email,pass1)
        my_User.save()
        return redirect('Login')

    return render(request,"SignUp.html")

def Login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        request.session["Myuser"] = username
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("User Nor valid")


    return render(request,"Login.html")

def HomePage(request):
    UserName = request.session["Myuser"]
    return render(request,"Welcome.html",{"Name": UserName})

def LogoutPage(request):
    logout(request)
    return redirect('login')

    # =================send mail=============
def SendEmail(request):
    send_mail(
        "Testing Email Using Django",
        "Hiii... .there",
        "govindchoudhary844@gmail.com",
        ["govind@acem.edu.in","aryanchaudhary8447@gmail.com","govindchoudhary844@gmail.com"],
        fail_silently=False,
    )
    return HttpResponse("Email Successfully Sent...")