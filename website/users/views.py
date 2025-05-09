from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def reg(request):
    if request.user.is_authenticated:
        return redirect('home:index')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                login(request, form.save())
                return redirect('home:index')
        else:
            form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def log(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home:index')
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def out(request):
    logout(request)
    return redirect('home:index')