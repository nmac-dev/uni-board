from django.shortcuts import render

# Create your views here.

def account(response):
    return render(response, "account/account.html", {})