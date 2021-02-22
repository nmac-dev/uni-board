from django.shortcuts import render

# Create your views here.

def quiz(response):
    return render(response, "quiz/quiz.html", {})