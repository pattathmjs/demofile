from django.http import HttpResponse
from django.shortcuts import render
from . models import movie
# Create your views here.
def index(request):
    Movie= movie.objects.all()
    context={'movielist':Movie}

    return render(request,'index.html',context)
def detail(request,movieid):
    Movie=movie.objects.get(id=movieid)
    return render(request,"detail.html",{'movie':Movie})