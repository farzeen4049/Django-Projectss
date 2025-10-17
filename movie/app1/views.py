# from django.shortcuts import render
# from app1.forms import  MovieForm
# from app1.models import Moviedetail
#
#
#
# # Create your views here.
#
# def home(request):
#
#         b=Moviedetail.objects.all()
#         context={"movie":b}
#         return render(request,'movielist.html')
#
#
# def add(request):
#     if(request.method=="POST"):
#         from_instance=MovieForm(request.POST,request.FILES)
#         if from_instance.is_valid():
#            from_instance.save()
#            return render(request,'addmovie.html')
#     if (request.method == "GET"):
#         from_instance=MovieForm(request.GET)
#         context={'form':from_instance}
#         return render(request, 'addmovie.html',context)


from django.shortcuts import render, redirect

from app1.forms import MovieForm
from app1.models import Moviedetail

# Create your views here.

def movielist(request):
        b =Moviedetail.objects.all()  # to read all record from table
        context = {'Moviedetail': b}
        return render(request,'movielist.html',context)

def addmovie(request):
    if request.method=="POST": #after submission
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            context={'form':form_instance}
            return render(request,'addmovie.html',context)

    if request.method=="GET":
        form_instance=MovieForm()
        context={'form':form_instance}
        return  render(request,'addmovie.html',context)

def moviedetails(request,i):
    if request.method=="GET":
        b=Moviedetail.objects.get(id=i)
        context={'movie':b}
        return render(request,'moviedetails.html',context)

def update(request,i):
    if request.method=="POST":
        b=Moviedetail.objects.get(id=i)
        form_instance=MovieForm(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            redirect('app1:movielist')

    if request.method=="GET":
        b=Moviedetail.objects.get(id=i)
        form_instance=MovieForm(instance=b)
        context={'movie':form_instance}
        return render(request,'update.html',context)

def delete(request,i):
    b=Moviedetail.objects.get(id=i)
    b.delete()
    return redirect('app1:movielist')