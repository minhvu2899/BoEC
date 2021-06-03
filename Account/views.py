from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as logouts
from django.contrib.auth import login as logins
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from Account.models import SignUpForm
from user.models import CustomerUser
 
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    return render(request,"homepage/home-page.html",{"user":request.user})
def register(request):
    User = get_user_model()
    print(User)
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:login")
    else:
        form =SignUpForm()
    return render(request,"Account/register.html",{"form":form})

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            if user is None:
                return HttpResponse("Tai khoan khong ton tai")
            logins(request,user)
          
           
            return redirect('account:home')
    else:
        form=AuthenticationForm() 
    return render(request,"Account/login.html",{"form":form})

def logout(request):
    logouts(request)
    return redirect('/')