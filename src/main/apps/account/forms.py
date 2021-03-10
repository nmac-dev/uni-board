from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.safestring import mark_safe

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    terms_and_conditions = forms.BooleanField()
    

    class Meta:
        model = User   #register going to save to User model
        fields = ('username','email','password1','password2','terms_and_conditions')

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']