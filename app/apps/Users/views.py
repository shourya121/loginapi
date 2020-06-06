from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Users.models import custom_user
from .serializers import UserLoginSerializer
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

@login_required
def welcome(request):
    return render(request,"welcome.html")






def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form.set_password(form.password)
            form.save()

        else:
            print("error")

    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:


            if user.is_active:

                login(request,user)

                return HttpResponseRedirect(reverse('profile'))

            else:
               HttpResponse("Please register first")
        else:
            print("someone tried to login and failed")
            print("Username:{} and password {}".format(username,password))
            return HttpResponse("Invalid login details")

    else:
         return render(request,'login.html',{})


@login_required
def profile(request):
    return render(request,'profile.html')

class UserLogin(APIView):
    serializer_class=UserLoginSerializer
    def post(self,request, *args, **kwargs):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
