import math

from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.

def addition(request):
    if(request.method=='POST'):
        print(request.POST)
        n1=int(request.POST['n1'])
        n2=int(request.POST['n2'])
        s=n1+n2
        context={'result':s}
        return render(request,'addition.html',context)

    if(request.method=='GET'):
        return render(request, 'addition.html')

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
        n1=int(request.POST['n1'])
        n2=int(request.POST['n2'])
        s=n1/(n2**2)
        context={'result':s}
        return render(request,'bmi.html',context)

    if(request.method=='GET'):
        return render(request, 'bmi.html')





