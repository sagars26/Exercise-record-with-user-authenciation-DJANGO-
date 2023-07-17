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

@unauthorized_user
def registerPage(request):
    form=createUserForm()
    if request.method=='POST':
        form=createUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='user')
            user.groups.add(group)
            email=form.cleaned_data.get('email')
            Customer.objects.create(user=user, name=username,email=email)
            messages.success(request,'Account created for '+username)
            return redirect('login')
    context={'form':form}
    return render(request,'register.html',context)

@unauthorized_user
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is invalid')
    return render(request,'login.html')


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

def userPage(request):
    user=request.user
    cust=user.customer
    exerciselist=Exerc.objects.filter()
    myfilter = exerciseFilter(request.GET,queryset=exerciselist)
    exerciselist=myfilter.qs
    total=Userexer.objects.all()
    myexercise=total.filter(customer=cust)
    cnt=myexercise.count()
    querysetexer=[]
    for e in myexercise:
        querysetexer.append(e.exerdone.all())
    finalexer=[]
    for items in querysetexer:
        for ex_er in items:
            finalexer.append(ex_er)
    totalCalories=0
    for exerci in finalexer:
        totalCalories+=exerci.calorie
    CalorieLeft=2000-totalCalories
    context={'CalorieLeft':CalorieLeft,'totalCalories':totalCalories,'cnt':cnt,'foodlist':finalexer,'fooditem':exerciselist,'myfilter':myfilter}
    return render(request,'user.html',context)

def addexercise(request):
    user=request.user
    cust=user.customer
    if request.method=="POST":
        form =addUserexitem(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=addUserexitem()
    context={'form':form}
    return render(request,'addUserexitem.html',context)
