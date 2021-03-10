from django.urls import path, include
from main.apps.account import views as user_views
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("",                 user_views.account,                                                      name="account"  ),
    path('register/',        user_views.register,                                                     name='register' ),
    path('login/',           auth_views.LoginView.as_view(   template_name='account/login.html'    ), name='login'    ),
    path('logout/',          auth_views.LogoutView.as_view(  template_name='account/logout.html'   ), name='logout'   ),
    path('profile/',         user_views.profile,                                                      name='profile'  ),
    path('profile/edit/',    user_views.edit_profile,                                                 name='edit_profile'),
    path('change-password/', user_views.change_password,                                              name='change_password'),
    path('terms',            user_views.terms,                                                        name='terms'),

## password recovery views
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'),
    name ='reset_password'),
    path('reset_password_Sent/', auth_views.PasswordResetDoneView.as_view(template_name='account/reset_password_Sent.html'),                      
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/reset_password_confirm.html'),                
    name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/reset_password_complete.html'),              
    name ='password_reset_complete'),
]

