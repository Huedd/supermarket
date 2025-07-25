from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.full_name


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    name = models.ForeignKey("RegisteredUser", on_delete=models.CASCADE, related_name="as_name")
    email = models.ForeignKey("RegisteredUser", on_delete=models.CASCADE, related_name="as_email")

    def __str__(self):
        return self.user.username


class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)

    def __str__(self):
        return self.user.username
