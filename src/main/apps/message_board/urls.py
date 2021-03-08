from django.urls import path
from .views import (
    Message_Board,
    Create_Post,
    Update_Post,
    Post_Detail,
    My_Posts
)

urlpatterns = [
    path('',                    Message_Board.as_view(),    name='message_board'),
    path('create/',             Create_Post.as_view(),      name='create_post'  ),
    path('<int:pk>/update/',    Update_Post.as_view(),      name='update_post'  ),
    path('<int:pk>/',           Post_Detail.as_view(),      name='post_detail' ),
    path('my_posts/',           My_Posts.as_view(),         name='my_posts'     ),
]