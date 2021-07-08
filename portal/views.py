from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
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
    user = request.user
    dev = developer.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        year = request.POST['year']
        contact = request.POST['contact']
        gen = request.POST['gender']
        dev.user.first_name = fname
        dev.user.last_name = lname
        dev.mobile = contact
        dev.gender = gen
        dev.year = year
        try:
            dev.save()
            dev.user.save()
            error = "no"
        except:
            error = "yes"
    d = {'dev':dev, 'error':error}
    return render(request, 'developer_home.html', d)


def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    rec = recruiter.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        year = request.POST['year']
        contact = request.POST['contact']
        gen = request.POST['gender']
        rec.user.first_name = fname
        rec.user.last_name = lname
        rec.mobile = contact
        rec.gender = gen
        rec.year = year
        try:
            rec.save()
            rec.user.save()
            error = "no"
        except:
            error = "yes"
    d = {'rec': rec, 'error': error}
    return render(request, 'recruiter_home.html', d)


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
        try:
            new_user = User.objects.create_user(first_name=fname, last_name=lname, username=email, password=pwd)
            developer.objects.create(user=new_user, year=year, mobile=contact, gender=gen, type="developer")
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
    dev = User.objects.filter(id=pid)
    dev.delete()
    return redirect('view_developers')


def delete_recruiter(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    rec = User.objects.filter(id=pid)
    rec.delete()
    return redirect('recruiter_all')


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


def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        cpwd = request.POST['cpwd']
        npwd = request.POST['npwd']
        try:
            user = User.objects.get(id=request.user.id)
            if user.check_password(cpwd):
                user.set_password(npwd)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'change_passwordadmin.html', d)


def change_password_developer(request):
    if not request.user.is_authenticated:
        return redirect('developer_login')
    error = ""
    if request.method == 'POST':
        cpwd = request.POST['cpwd']
        npwd = request.POST['npwd']
        try:
            user = User.objects.get(id=request.user.id)
            if user.check_password(cpwd):
                user.set_password(npwd)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'change_password_developer.html', d)


def change_password_recruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if request.method == 'POST':
        cpwd = request.POST['cpwd']
        npwd = request.POST['npwd']
        try:
            user = User.objects.get(id=request.user.id)
            if user.check_password(cpwd):
                user.set_password(npwd)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'change_password_recruiter.html', d)


def add_project(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if request.method == 'POST':
        title = request.POST['title']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        company = request.POST['company']
        location = request.POST['location']
        description = request.POST['description']
        skills = request.POST['skills']
        experience = request.POST['experience']
        compensation = request.POST['compensation']
        user = request.user
        rec = recruiter.objects.get(user=user)
        try:
            project.objects.create(recruiter=rec, start_date=start_date, end_date=end_date, title=title, company=company, location=location,
                                   description=description, skills=skills, experience=experience,
                                   compensation=compensation, creationdate=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_project.html', d)


def project_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    rec = recruiter.objects.get(user=user)
    projects = project.objects.filter(recruiter=rec)
    d = {'projects': projects}
    return render(request, 'project_list.html', d)


def edit_project(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    curr_project = project.objects.get(id=pid)
    if request.method == 'POST':
        title = request.POST['title']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        company = request.POST['company']
        location = request.POST['location']
        description = request.POST['description']
        skills = request.POST['skills']
        experience = request.POST['experience']
        compensation = request.POST['compensation']

        curr_project.title = title
        curr_project.company = company
        curr_project.location = location
        curr_project.description = description
        curr_project.skills = skills
        curr_project.experience = experience
        curr_project.compensation = compensation
        try:
            curr_project.save()
            error = "no"
        except:
            error = "yes"
        if start_date:
            try:
                curr_project.start_date = start_date
                curr_project.save()
            except:
                pass
        else:
            pass
        if end_date:
            try:
                curr_project.end_date = end_date
                curr_project.save()
            except:
                pass
        else:
            pass
    d = {'curr_project': curr_project, 'error': error}
    return render(request, 'edit_project.html', d)


