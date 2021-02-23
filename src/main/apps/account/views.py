from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created! Please log in!')
            return redirect('/account/login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})

def profile(request):
    return render(request, 'account/profile.html')

# Create your views here.

def account(response):
    return render(response, "account/account.html", {})

def edit_profile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        if not request.user.is_anonymous:
            form = EditProfileForm(instance = request.user)
            return render(request, 'account/edit_profile.html', {'form': form})
        else:
            return redirect('/account/login')



def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(data =request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        if not request.user.is_anonymous:
            form = PasswordChangeForm(user = request.user)
            return render(request, 'account/change_password.html', {'form': form})
        else:
            return redirect('/account/login')