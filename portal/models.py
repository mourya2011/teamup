from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class developer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    year = models.CharField(max_length=4)
    gender = models.CharField(max_length=10)
    type = models.CharField(max_length=15)

    def _str_(self):
        return self.user.username


class recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    year = models.CharField(max_length=4)
    gender = models.CharField(max_length=10)
    type = models.CharField(max_length=15)
    status = models.CharField(max_length=20)

    def _str_(self):
        return self.user.username


class project(models.Model):
    recruiter = models.ForeignKey(recruiter, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)
    compensation = models.FloatField(max_length=10)
    description = models.CharField(max_length=300)
    experience = models.CharField(max_length=50)
    company = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50)
    skills = models.CharField(max_length=300)
    creationdate = models.DateField()

    def _str_(self):
        return self.title

