from django.urls import path

from app1 import views


app_name='app1'
urlpatterns = [
    path('',views.Movielist.as_views(),name="movielist"),
    path('addmovie', views.Addmovie.as_views(), name="addmovie"),
    path('moviedetails/<int:i>',views.Moviedetails.as_views(),name='moviedetails'),
    path('update/<int:i>',views.Update.as_views(),name='update'),
    path('delete/<int:i>',views.Delete.as_views(),name='delete'),

]