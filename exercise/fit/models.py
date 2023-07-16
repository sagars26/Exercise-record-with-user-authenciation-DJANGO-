from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.name)
    
class Category(models.Model):
    options=(
        ('chest','chest'),
        ('back','back'),
        ('arms','arms'),
        ('legs','legs'),
        ('core','core')
    )
    name=models.CharField(max_length=50,choices=options)
    def __str__(self):
        return self.name
    
class Exerc(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    rep = models.IntegerField(default=1,null=True,blank=True)
    set = models.IntegerField(default=1,null=True,blank=True)
    weight = models.IntegerField(default=1,null=True,blank=True)
    calorie=models.DecimalField(max_digits=5,decimal_places=2,default=0,blank=True)
    
    
    def __str__(self):
        return str(self.name)
    
    #for user page-------------------------------------------------------------
class Userexer(models.Model):
    customer = models.ManyToManyField(Customer ,blank=True)
    exerdone=models.ManyToManyField(Exerc)