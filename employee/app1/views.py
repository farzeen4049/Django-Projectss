from django.shortcuts import render, redirect
from app1.forms import Employeeform
from app1.models import Employee
# Create your views here.
def home(request):
    b=Employee.object.all()
    context={'employee':b}
    return render(request,'home.html',context)

def add(request):
    if request.method=='POST':
        f=Employeeform(request.POST,request.FILES)
        if f.is_valid():
            f.save()
            return redirect('app1:add')

    if request.method=='GET':
        f=Employeeform()
        context={"form":f}
        return render(request,'add.html',context)

# def view(request):
#     if request.method=="GET":
#         f=Employee.objects.all()
#         context={'form':f}
#         return render(request,'view.html',context)
