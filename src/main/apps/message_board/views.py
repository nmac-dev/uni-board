from django.shortcuts           import render
from .models                    import User_Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
#   Views

class Message_Board(ListView):
    model = User_Post
    template_name = 'message_board/message_board.html'
    context_object_name = 'user_posts'
    ordering = ['-date_time']                           # Orders to most recent date

class User_Post_Detail(DetailView):
    model = User_Post