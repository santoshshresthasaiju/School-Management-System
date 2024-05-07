from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from registration.forms import LoginForm, CreateUserForm
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def homepage(request):
    

    return render(request, 'registration/index.html')

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)

                return redirect('home')
    else:
        initial_data = {'username':'', 'password':''}
        form = LoginForm(initial=initial_data)
    context = {'loginform':form}

    return render(request, 'registration/login.html',context=context)

def register_view(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        initial_data = {'username':'', 'email':'', 'password1':'','password2':''}
        form = CreateUserForm(initial=initial_data)
    context = {'registerform':form}

    return render(request, 'registration/register.html', context=context)
    
@login_required(login_url="login")
def logout_view(request):
    auth.logout(request)
    return redirect('login')

