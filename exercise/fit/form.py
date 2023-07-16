from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class exerciseForm(ModelForm):
    class Meta:
        model=Exerc
        fields="__all__"

class addUserexitem(ModelForm):
    class Meta:
        model=Userexer
        fields="__all__"
        
class createUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']