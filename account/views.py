from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import LoginForm




# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'nav.html')


def add_user(request):
    if request.method=='POST':
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/login')
    else:
        f=UserCreationForm
        context={'form':f}
        return render(request,'adduser.html',context)
    
# Create your LoginForm here.


def loginform(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request, username=uname, password=passw)
        if user is not None:
            request.session['uid'] = user.id
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('/login')
    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'login.html', context)

def logout_v(request):
    logout(request)
    return redirect('/login')

def base2(request):
    return render(request,'header2.html')






            
            
   
