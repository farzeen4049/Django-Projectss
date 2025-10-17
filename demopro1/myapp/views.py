from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
#
# def first(request):
#     return HttpResponse("First page")
#
# def second(request):
#     return HttpResponse("Second page")

def first(request):
    context={'name':'Arun','age':23}
    return render(request,'first.html',context)
def second(request):
    return render(request,'second.html')
