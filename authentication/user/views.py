from django.shortcuts import render,redirect
from django.views import View
from pyexpat.errors import messages


# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'home.html')

from user.forms import SignupForm,LoginForm
from django.contrib.auth.forms import UserCreationForm
class Register(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('login')
        else:
            print('error')
            return render(request,'register.html',{'form':form_instance})
    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)


from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
class Userlogin(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)
                #authenticate() return user object if user with the given username and password
                #else returns none

            if user:  #if user exists
                login(request, user) # login() add the current user into session
                return redirect('home')
            else:
                # print("Invalid User") to show in page
                messages.error(request,'Invalid User')
                return render(request,'login.html',{'form':form_instance})


    def get(self,request):
        form_instance = LoginForm()
        context = {'form': form_instance}
        return render(request,'login.html',context)
class Userlogout(View):
    def get(self,request):
        logout(request)
        return  redirect('login')


