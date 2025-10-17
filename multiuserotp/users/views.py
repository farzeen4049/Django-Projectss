from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
# Create your views here.
from django.views import View
from django.contrib import messages
from users.forms import SignupForm,LoginForm


from django.core.mail import send_mail
from users.models import Customuser

class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Register(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.save(commit=False)
            u.is_active=False
            u.save()
            u.generate_otp()
            send_mail(
                "Django Auth OTP",
                u.otp,
                "farzeen4049@gmail.com",
                [u.email],
                fail_silently=False,
            )
            return redirect('users:otp')
        else:
            print('invalid credentials ')

            return render(request,'register.html',{'form':form_instance})
    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)

class Userlogin(View):
    def get(self,request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request,'login.html',context)

    def post(self,request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            u = form_instance.cleaned_data['username']
            p = form_instance.cleaned_data['password']
            user=authenticate(username=u,password=p)
            if user and user.is_superuser==True:
                login(request,user)
                return redirect('users:adminhome')
            elif user and user.role=="student":
                login(request,user)
                return redirect('users:studenthome')
            elif user and user.role=="teacher":
                login(request,user)
                return redirect('users:teacherhome')
            else:
                messages.error(request,'Invalid User')
                return render(request,'login.html',{'form': form_instance})

class Userlogout(View):
    def get(self,request):
        logout(request)
        return redirect('users:login')

class Adminhome(View):
    def get(self,request):
        return render(request,'adminhome.html')

class Studenthome(View):
    def get(self,request):
        return render(request,'studenthome.html')

class Teacherhome(View):
    def get(self,request):
        return render(request,'teacherhome.html')

class Otp_verefiction(View):
    def post(self,request):
        otp=request.POST['otp']
        try:
            u=Customuser.objects.get(otp=otp)
            u.is_verified=True
            u.is_active=True
            u.otp=None
            u.save()
            return redirect('users:login')
        except:
            messages.error(request,'Invalid Otp')
            return redirect('users:otp')

    def get(self,request):
        return render(request,'otp.html')