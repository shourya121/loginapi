from rest_framework_mongoengine import serializers
from .models import User_info

class UserSerializer(serializers.DocumentSerializer):

    class Meta():
        model=User_info
        fields=('name','address','email',"username","password")
