from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group
from .filters import exerciseFilter




@login_required(login_url='login')
@admin_only
def home(request):
    chest=Category.objects.filter(name='chest')[0].exerciselist_set.all()[:5]
    back=Category.objects.filter(name='back')[0].exerciselist_set.all()[:5]
    legs=Category.objects.filter(name='legs')[0].exerciselist_set.all()[:5]
    arms=Category.objects.filter(name='arms')[0].exerciselist_set.all()[:5]
    core=Category.objects.filter(name='core')[0].exerciselist_set.all()[:5]
    customers=Customer.objects.all()
    context={'chest':chest,
              'back':back,
              'legs':legs,
              'arms':arms,
              'core':core,
              'customers':customers,
            }
    return render(request,'main.html',context)
