from django.urls import path

from app1 import views


app_name='app1'
urlpatterns = [
    path('',views.movielist,name="movielist"),
    path('addmovie', views.addmovie, name="addmovie"),
    path('moviedetails/<int:i>',views.moviedetails,name='moviedetails'),
    path('update/<int:i>',views.update,name='update'),
    path('delete/<int:i>',views.delete,name='delete'),

]