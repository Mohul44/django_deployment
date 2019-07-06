from django import forms
from djago.contrib.auth import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.model):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
        
