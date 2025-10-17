

from django.shortcuts import render, redirect

from app1.forms import MovieForm
from app1.models import Moviedetail

from django.views import View

# Create your views here.

class Movielist(View):
    def get(self,request):
        b =Moviedetail.objects.all()  # to read all record from table
        context = {'Moviedetail': b}
        return render(request,'movielist.html',context)

class Addmovie(View):
    def post(self,request): #after submission
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            context={'form':form_instance}
            return render(request,'addmovie.html',context)

    def get(self,request):
        form_instance=MovieForm()
        context={'form':form_instance}
        return  render(request,'addmovie.html',context)

class Moviedetails(View):
    def get(self,request,i):
        b=Moviedetail.objects.get(id=i)
        context={'movie':b}
        return render(request,'moviedetails.html',context)

class Update(View):
    def post(self,request,i):
        b=Moviedetail.objects.get(id=i)
        form_instance=MovieForm(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            redirect('app1:movielist')

    def get(self,request,i):
        b=Moviedetail.objects.get(id=i)
        form_instance=MovieForm(instance=b)
        context={'movie':form_instance}
        return render(request,'update.html',context)

class Delete(View):
    def get(self,request,i):
        b=Moviedetail.objects.get(id=i)
        b.delete()
        return redirect('app1:movielist')