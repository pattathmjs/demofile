from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def demo(request):
    return render(request,'index.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']

        password = request.POST['password']
        confirmpassword = request.POST['confirm password']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect("register")

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect("register")

        return redirect('login')

    return render(request,"register.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "invalid credentials")
            return redirect("login")
    return render(request, "login.html")
def details(request):
    if request.method=='POST':
        username=request.POST['username']
        date=request.POST['date']
        age=request.POST['age']
        phonenumber=request.POST['phonenumber']
        email=request.POST['email']
        address=request.POST['address']

    return render(request,'details.html')
def home(request):
    return render(request,'home.html')
def end(request):
    return render(request,'end.html')


