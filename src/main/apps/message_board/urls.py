from django.urls import path
from .views import (
    Message_Board,
    User_Post_Detail
)

urlpatterns = [
    path("",                Message_Board.as_view(),    name="message_board"),
    path('<int:pk>/',       User_Post_Detail.as_view(), name='user_post'    ),
]