from django.contrib                 import admin
from main.apps.message_board.models import User_Post, User_Comment
from main.apps.quiz.models          import Quiz_Model

# Models
admin.site.register(User_Post)
admin.site.register(User_Comment)
admin.site.register(Quiz_Model)