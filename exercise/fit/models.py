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