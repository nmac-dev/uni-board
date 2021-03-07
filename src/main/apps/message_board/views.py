from django.shortcuts           import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls                import reverse
from .models                    import User_Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
#   Views

class Create_Post(LoginRequiredMixin, CreateView):
    model           = User_Post
    fields          = ['post_subject', 'post_content']
    template_name   = "message_board/user_create_post.html"
    post_id = None

    def form_valid(self, form):
        form.instance.post_user = self.request.user
        post            =   form.save()
        self.post_id    =   post.post_id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('user_post', kwargs={'pk': self.post_id})

class Message_Board(ListView):
    model               = User_Post
    ordering            = ['-post_date']                   # Orders to most recent date
    context_object_name = 'user_posts'
    template_name       = 'message_board/message_board.html'

class User_Post_Detail(DetailView):
    model = User_Post


class My_Posts(LoginRequiredMixin, ListView):
    model               = User_Post
    ordering            = ['-post_date']                   # Orders to most recent date
    context_object_name = 'user_posts'
    template_name       = 'message_board/my_posts.html'