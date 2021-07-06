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

