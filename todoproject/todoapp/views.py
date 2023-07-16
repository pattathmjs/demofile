from django.shortcuts import render,redirect
from . models import Task
from . form import Todoform
# Create your views here.
def add(request):
    task1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority = request.POST.get('priority','')
        task=Task(name=name,priority=priority)
        task.save()
    return render(request,'home.html',{'task1':task1})

def details(request):
    task=Task.objects.all()
    return render(request,'details.html',{'task':task})
def delete(request,taskid):
    if request.method=='POST':
        task=Task.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
        task=Task.objects.get(id=id)
        f=Todoform(request.POST or None,instance=task)
        if f.is_valid():
            f.save()
            return redirect('/')
        return render(request,'edits.html',{'f':f,'task':task})
