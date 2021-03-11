from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, EditProfileForm, UpdateProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

AcLog = '/account/login'

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created! Please log in!')
            return redirect(AcLog)
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})

def profile(request):
    return render(request, 'account/profile.html')

def terms(request):
    return render(request, 'account/terms.html')

# Create your views here.

def account(response):
    return render(response, "account/account.html", {})

@login_required
def edit_profile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance = request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)
            
    return render(request, 'account/edit_profile.html', {'form': form, 'p_form':p_form})



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
            return redirect(AcLog)