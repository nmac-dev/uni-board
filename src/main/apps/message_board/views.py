from django.shortcuts import render

# Create your views here.

def message_board(response):
    return render(response, "message_board/message_board.html", {})