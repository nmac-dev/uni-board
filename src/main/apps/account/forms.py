from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.safestring import mark_safe
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    terms_and_conditions = forms.BooleanField()
    

    class Meta:
        model = User   #register going to save to User model
        fields = ['username','email','password1','password2','is_staff', 'terms_and_conditions']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email',]

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']