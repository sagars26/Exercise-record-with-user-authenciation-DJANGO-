from django.http import HttpResponse
from django.shortcuts import redirect


#this function will identify unauthorised users
def unauthorized_user(view_func): 
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func