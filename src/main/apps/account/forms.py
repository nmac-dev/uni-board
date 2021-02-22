from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User   #register going to save to User model
        fields = ['username','email','password1','password2']

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'email']