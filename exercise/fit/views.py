from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group
from .filters import exerciseFilter
from .form import exerciseForm




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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def exerciselist(request):
    chest=Category.objects.filter(name='chest')[0].exerciselist_set.all()
    cht=chest.count()
    back=Category.objects.filter(name='back')[0].exerciselist_set.all()
    bck=back.count()
    legs=Category.objects.filter(name='legs')[0].exerciselist_set.all()
    lgs=legs.count()
    arms=Category.objects.filter(name='arms')[0].exerciselist_set.all()
    ars=arms.count()
    core=Category.objects.filter(name='arms')[0].exerciselist_set.all()
    cre=core.count()
    context={'chest':chest,
              'cht':cht,
              'bck':bck,
              'lgs':lgs,
              'ars':ars,
              'cre':cre,
              'back':back,
              'legs':legs,
              'arms':arms,
              'core':core,
            }
    return render(request,'exeriselist.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createxercise(request):
    form = exerciseForm()
    if request.method == 'POST':
        form = exerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'createxercise.html',context)


