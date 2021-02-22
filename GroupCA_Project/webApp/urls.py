from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webApp-home'),
    path('about/', views.about, name='webApp-about'),
]