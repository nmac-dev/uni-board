from django.shortcuts import render
from .models import Leaderboard
from django.views.generic import (
    ListView,
)

# Create your views here.

class leaderboard(ListView):
    model               = Leaderboard
    ordering            = ['-points']                   # Orders to most points
    context_object_name = 'leaderboard'
    template_name       = 'leaderboard/leaderboard.html'