from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = SignupForm()
    else:
        fm = SignupForm()

    return render(request, 'signup.html', {'form': fm})



def user_login(request):
    if request.method=='POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
        
    else:
        fm = AuthenticationForm()

    return render(request, 'login.html', {'form': fm}) 


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'name': request.user})
    
    else:
        return HttpResponseRedirect('/login/')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')
