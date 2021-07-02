"""intern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('admin_login', admin_login, name="admin_login"),
    path('student_login', student_login, name="student_login"),
    path('recruiter_login', recruiter_login, name="recruiter_login"),
    path('student_signup', student_signup, name="student_signup"),
    path('recruiter_signup', recruiter_signup, name="recruiter_signup"),
    path('student_home', student_home, name="student_home"),
    path('recruiter_home', recruiter_home, name="recruiter_home"),
    path('Logout', Logout, name="Logout"),
]
