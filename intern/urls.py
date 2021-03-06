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
    path('developer_login', developer_login, name="developer_login"),
    path('recruiter_login', recruiter_login, name="recruiter_login"),
    path('developer_signup', developer_signup, name="developer_signup"),
    path('recruiter_signup', recruiter_signup, name="recruiter_signup"),
    path('developer_home', developer_home, name="developer_home"),
    path('recruiter_home', recruiter_home, name="recruiter_home"),
    path('admin_home', admin_home, name="admin_home"),
    path('Logout', Logout, name="Logout"),
    path('view_developers', view_developers, name="view_developers"),
    path('delete_developer/<int:pid>', delete_developer, name="delete_developer"),
    path('delete_recruiter/<int:pid>', delete_recruiter, name="delete_recruiter"),
    path('recruiter_pending', recruiter_pending, name="recruiter_pending"),
    path('change_status/<int:pid>', change_status, name="change_status"),
    path('recruiter_accepted', recruiter_accepted, name="recruiter_accepted"),
    path('recruiter_rejected', recruiter_rejected, name="recruiter_rejected"),
    path('recruiter_all', recruiter_all, name="recruiter_all"),
    path('change_passwordadmin', change_passwordadmin, name="change_passwordadmin"),
    path('change_password_developer', change_password_developer, name="change_password_developer"),
    path('change_password_recruiter', change_password_recruiter, name="change_password_recruiter"),
    path('add_project', add_project, name="add_project"),
    path('project_list', project_list, name="project_list"),
    path('edit_project/<int:pid>', edit_project, name="edit_project"),
]
