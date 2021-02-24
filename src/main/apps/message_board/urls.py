from django.urls import path
from .views import (
    Message_Board,
    Create_Post,
    User_Post_Detail,
    My_Posts
)

urlpatterns = [
    path('',                Message_Board.as_view(),    name='message_board'    ),
    path('create/',         Create_Post.as_view(),      name='user_create_post' ),
    path('<int:pk>/',       User_Post_Detail.as_view(), name='user_post'        ),
    path('my_posts/',       My_Posts.as_view(),         name='my_posts'         ),
]