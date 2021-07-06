from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, 'index.html')


def admin_login(request):
    error = ""
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(username=uname, password=pwd)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'admin_login.html',d)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')


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


def view_developers(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = developer.objects.all()
    d = {'data': data}
    return render(request, 'view_developers.html', d)


def delete_developer(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    dev = developer.objects.filter(user_id=pid)
    dev.delete()
    return redirect('view_developers')


def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = recruiter.objects.filter(status="pending")
    d = {'data': data}
    return render(request, 'recruiter_pending.html', d)


def change_status(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    rec = recruiter.objects.get(user_id=pid)
    if request.method == 'POST':
        s = request.POST['status']
        if s == "Accept":
            s = "accepted"
        else:
            s = "rejected"
        rec.status = s
        try:
            rec.save()
            error = "no"
        except:
            error = "yes"
    d = {'rec': rec, 'error': error}
    return render(request, 'change_status.html', d)


def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = recruiter.objects.filter(status="accepted")
    d = {'data': data}
    return render(request, 'recruiter_accepted.html', d)


def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = recruiter.objects.filter(status="rejected")
    d = {'data': data}
    return render(request, 'recruiter_rejected.html', d)


def recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = recruiter.objects.all()
    d = {'data': data}
    return render(request, 'recruiter_all.html', d)
