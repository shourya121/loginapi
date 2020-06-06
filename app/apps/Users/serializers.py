from django.db import models
from rest_framework import serializers
from Users.models import custom_user
from django.db.models import Q
from django.contrib.auth import get_user_model

User= get_user_model()
print(User.objects.all())
class UserLoginSerializer(serializers.ModelSerializer):
    username = models.CharField(max_length=100)#,required=False ,allow_blank=True)
    email=models.EmailField()#label="Email Address",required=False ,allow_blank=True)
    class Meta:
        model = User
        fields=("email","username","password")
        extra_kwargs={
                        "password":{"write_only": True}
        }

    def validate_data(self,data):
        user_obj = None
        email = data.get("email",None)
        username = data.get("username",None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A Username or email is required to login.")

        user = User.objects.filter(
                Q(email=email) |
                Q(username=username)
        ).distinct()
        print(user)
        if user.exists() and user.count() == 1:
            user_obj=user.first()
        else:
            raise ValidationError("This Username/Email is not valid!")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again.")

        return data
