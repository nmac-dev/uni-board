from django.urls import path

from . import views

urlpatterns = [
    path("", views.leaderboard.as_view(), name="leaderboard"),
]