from django.urls import path
from . import views


urlpatterns = [

    path('',views.demo,name='demo'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('details', views.details, name='details'),
    path('home', views.home, name='home'),
    path('end', views.end, name='end'),

]
