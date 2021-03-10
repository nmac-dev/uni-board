from django.urls import path
from .views import (
    Quiz_Home,
    Quiz_Detail,
    Create_Quiz,
    Update_Quiz,
    Delete_Quiz,
    My_Quizzes,
    Quiz_Results
)

urlpatterns = [
    path("",                    Quiz_Home.as_view(),        name="quiz_home"    ),
    path('<int:pk>/',           Quiz_Detail.as_view(),      name='take_quiz'    ),
    path('create/',             Create_Quiz.as_view(),      name='create_quiz'  ),
    path('<int:pk>/update/',    Update_Quiz.as_view(),      name='update_quiz'  ),
    path('<int:pk>/delete/',    Delete_Quiz.as_view(),      name='delete_quiz'  ),
    path('my_posts/',           My_Quizzes.as_view(),       name='my_quizzes'   ),
    path('results',    Quiz_Results,      name='quiz_results'),
]