from django import forms
from .models import User_info
from mongodbforms import DocumentForm


class Newuser(DocumentForm):
    password=forms.CharField(widget=forms.PasswordInput())



    class Meta():
        document=User_info
        fields= ('name','email','address','username','password')
