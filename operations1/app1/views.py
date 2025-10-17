import math

from django.db.models.expressions import result
from django.shortcuts import render
from django.template.context_processors import request
from app1.forms import AdditionForm
from app1.forms import BmiForm



# Create your views here.

def addition(request):

    if (request.method=='POST'):
        print(request.POST)

        #create from instance using submitted data
        from_instance=AdditionForm(request.POST)
        #ceck weather the data is valid
        if from_instance.is_valid():

                #proccessing data
            data=from_instance.cleaned_data
            print(data)
            n1=data['num1']
            n2=data['num2']
            sum=int(n1)+int(n2)
            context={'result':sum,'form':from_instance}

            return render(request,'addition.html',context)

    if (request.method=='GET'):
        form_instance=AdditionForm()
        context={'form':form_instance}
        return render(request,'addition.html',context)

def factorial(request):
    if (request.method == 'GET'):
        return render(request, 'factorial.html')

    if(request.method=='POST'):
        print(request.POST)
        fac= int(request.POST['fact'])
        s=math.factorial(fac)
        context={'result':s}
        return render(request,'factorial.html',context)

def bmi(request):
    if(request.method=='POST'):
        print(request.POST)

        from_instance=BmiForm(request.POST)

        if from_instance.is_valid():
            data=from_instance.cleaned_data
            h=int(request.POST['height'])
            w=int(request.POST['weight'])
            b=h/(w**2)
            context={'result':b,'form':from_instance}
            return render(request,'bmi.html',context)

    if(request.method=='GET'):
        form_instance=BmiForm()
        context = {'form': form_instance }
        return render(request, 'bmi.html',context)


from app1.forms import SignupForm,CalorieForm


def signup(request):

    if(request.method=='POST'):
        form_instance=SignupForm(request.POST)

        if form_instance.is_valid():
             data=form_instance.cleaned_data
             print(data)
             return render(request,'signup.html')


    if(request.method=='GET'):
          form_instance=SignupForm()
          context={'form':form_instance}
          return render (request,'signup.html',context)


def calorie(request):

    if(request.method=='POST'):
        form_instance=CalorieForm(request.POST)

        if form_instance.is_valid():
             data=form_instance.cleaned_data
             print(data)
             w=int(data['weight'])
             h=int(data['height'])
             a=int(data['age'])
             g=data['gender']
             al=float(data['activity_levels'])
             if g=='male':
                 bmr=10*w+6.25*h-5*a+5
             else:
                 bmr=10*w+6.25*h-5*a-161
             c=bmr*al
             context={'result':c,'from':form_instance}

             return render(request,'calorie.html')


    if(request.method=='GET'):
          form_instance=CalorieForm()
          context={'form':form_instance}
          return render (request,'calorie.html',context)


