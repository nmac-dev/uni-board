from django.shortcuts import render

# Create your views here.

def leaderboard(response):
    return render(response, "leaderboard/leaderboard.html", {})