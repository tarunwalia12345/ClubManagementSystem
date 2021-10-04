from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Form(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=" ")
    email=models.CharField(max_length=50,default="")
    ClubName=models.CharField(max_length=50, default="")
    RepresentativeName=models.CharField(max_length=50,default="")
    Contact=models.CharField(max_length=12, default=None)
    req_date_from=models.DateField(default='')
    req_date_to=models.DateField(default="")
    req_type=models.CharField(max_length=50,default="")
    req_purpose=models.TextField(max_length=50, blank=True, default="")
    alloted=models.IntegerField(default=0)
    Management_Comments=models.TextField(max_length=100, blank=True, default="")
    def __str__(self):
        return self.email   
    objects = models.Manager() 