from django.db import models
from mongoengine import *
from mongodbforms import DocumentForm
import os
import json



connect(
    db= "mydb",
    username= "Shourya",
    password= "casper1004",
    host='mongodb+srv://Shourya:casper1004@shourya-cm52a.mongodb.net/mydb?authSource=admin&replicaSet=Shourya-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true',
)
class User_info(Document):




    name=StringField(max_length=100)
    address=StringField(max_length=100)
    email=EmailField(max_length=100)
    username=StringField(max_length=100)
    password=StringField(max_length=100)




def json(self):
    form_dict= {
    "name" : self.name,
    "address" : self.address,
    "email" : self.email,
    "username":self.username,
    "password":self.password,
    }
    return json.dumps(form_dict)













#class User(models.Model):
