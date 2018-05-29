from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        if  request.POST['password'] ==  request.POST['password1']:
            try:
                user = User.objects.get(username=request.POST['username'])
                print('user')
                return render(request,'accounts/signup.html',{'user_error':'USER ALREADY EXISTS !!!'})                       
            except:
                print('okay')
                User.objects.create_user(request.POST['username'],request.POST['email'],password =  request.POST['password'])
                return render(request,'accounts/login.html')
        else:
            print("pass")
            return render(request,'accounts/signup.html',{'Error':'Password didn\'t Match'})            
        print("THE POST WOREKD")
    return render(request,'accounts/signup.html')

def login1(request):
    if request.method == "POST":
        print('up')
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        print('down')
        if user is not None:
            print('correct')
            login(request,user)
            if 'next' in request.POST:
                if request.POST['next'] is not None:
                    return redirect(request.POST['next'])
            return render(request,'accounts/login.html',{'error':'LOGGED IN Succesfully !!!'})
        else:
            return render(request,'accounts/login.html',{'error':'Credentials are INCORRECT !!!'})
    return render(request,'accounts/login.html')    