from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, 'index.html')


def admin_login(request):
    return render(request, 'admin_login.html')


def developer_home(request):
    if not request.user.is_authenticated:
        return redirect('developer_login')
    return render(request, 'developer_home.html')


def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    return render(request, 'recruiter_home.html')


def Logout(request):
    logout(request)
    return redirect('index')


def developer_login(request):
    error = ""
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(username=uname, password=pwd)
        if user:
            try:
                user1 = developer.objects.get(user=user)
                if user1.type == "developer":
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"

        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'developer_login.html', d)


def recruiter_login(request):
    error = ""
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(username=uname, password=pwd)
        if user:
            try:
                user1 = recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status != "pending":
                    login(request, user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"

        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'recruiter_login.html', d)


def developer_signup(request):
    error = ""
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        year = request.POST['year']
        email = request.POST['email']
        pwd = request.POST['pwd']
        contact = request.POST['contact']
        gen = request.POST['gender']
        try :
            new_user = User.objects.create_user(first_name=fname, last_name=lname, username=email, password=pwd)
            developer.objects.create(user= new_user, year= year,mobile=contact, gender= gen, type="developer")
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'developer_signup.html', d)


def recruiter_signup(request):
    error = ""
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        year = request.POST['year']
        email = request.POST['email']
        pwd = request.POST['pwd']
        contact = request.POST['contact']
        gen = request.POST['gender']
        try:
            new_user = User.objects.create_user(first_name=fname, last_name=lname, username=email, password=pwd)
            recruiter.objects.create(user=new_user, year=year, mobile=contact, gender=gen, type="recruiter", status="pending")
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'recruiter_signup.html', d)
