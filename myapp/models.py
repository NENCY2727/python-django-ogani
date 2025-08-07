from django.db import models # type: ignore
from .models import*
from django.contrib import messages  # type: ignore



# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    department = models.CharField(max_length=50)
    phone = models.BigIntegerField()

    def __str__(self):
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class department(models.Model):
    department_name=models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

class colorfilter(models.Model):
    color_name=models.CharField(max_length=20)

    def __str__(self):
        return self.color_name
    
class size(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class product(models.Model):
    pname=models.CharField(max_length=30)
    price=models.IntegerField(max_length=20)
    image=models.ImageField(upload_to="image")
    department=models.ForeignKey(department,on_delete=models.CASCADE,blank=True,null=True)
    colorfilter=models.ForeignKey(colorfilter,on_delete=models.CASCADE,blank=True,null=True)
    size=models.ForeignKey(size,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.pname           
    


    
