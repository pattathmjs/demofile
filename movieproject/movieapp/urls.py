
from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movieid>/',views.detail, name='detail')
]