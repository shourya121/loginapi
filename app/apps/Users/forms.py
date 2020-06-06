from django import forms
from Users.models import custom_user
from django.contrib.auth.forms import UserCreationForm
from mongodbforms import DocumentForm



class UserRegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = custom_user

        fields = ['username', 'email','password']
