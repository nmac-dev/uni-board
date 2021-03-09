from django.shortcuts           import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls                import reverse
from .models                    import Quiz_Model
from .forms                     import Quiz_Model_Form
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Quiz Home Page
class Quiz_Home(ListView):
    model               = Quiz_Model
    ordering            = ['-date']                   # Orders to most recent date
    context_object_name = 'quiz_models'
    template_name       = 'quiz/quiz_home.html'

class Quiz_Detail(DetailView):
    model = Quiz_Model
    template_name   = "quiz/take_quiz.html"

class Create_Quiz(LoginRequiredMixin, CreateView):
    model         = Quiz_Model
    fields      =   [   'title', 
                        'desc',
                        # Each Row is a question set
                        'Question_1', 'Question_1_Option_1', 'Question_1_Option_2','Question_1_Option_3','Question_1_Option_4', 'Question_1_Correct_Answer',
                        'Question_2', 'Question_2_Option_1', 'Question_2_Option_2','Question_2_Option_3','Question_2_Option_4', 'Question_2_Correct_Answer',
                        'Question_3', 'Question_3_Option_1', 'Question_3_Option_2','Question_3_Option_3','Question_3_Option_4', 'Question_3_Correct_Answer',
                        'Question_4', 'Question_4_Option_1', 'Question_4_Option_2','Question_4_Option_3','Question_4_Option_4', 'Question_4_Correct_Answer',
                        'Question_5', 'Question_5_Option_1', 'Question_5_Option_2','Question_5_Option_3','Question_5_Option_4', 'Question_5_Correct_Answer',
                        'Question_6', 'Question_6_Option_1', 'Question_6_Option_2','Question_6_Option_3','Question_6_Option_4', 'Question_6_Correct_Answer',
                        'Question_7', 'Question_7_Option_1', 'Question_7_Option_2','Question_7_Option_3','Question_7_Option_4', 'Question_7_Correct_Answer',
                        'Question_8', 'Question_8_Option_1', 'Question_8_Option_2','Question_8_Option_3','Question_8_Option_4', 'Question_8_Correct_Answer',
                        'Question_9', 'Question_9_Option_1', 'Question_9_Option_2','Question_9_Option_3','Question_9_Option_4', 'Question_9_Correct_Answer',
                        'Question_10', 'Question_10_Option_1', 'Question_10_Option_2', 'Question_10_Option_3', 'Question_10_Option_4', 'Question_10_Correct_Answer',
                    ]
    template_name   = "quiz/create_quiz.html"
    quiz_id = None
    #form_class = Quiz_Model_Form

    # Validate user is logged in
    def form_valid(self, form):
        form.instance.creator = self.request.user
        quiz            =   form.save()
        self.quiz_id    =   quiz.quiz_id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('take_quiz', kwargs={'pk': self.quiz_id})

class Update_Quiz(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model           = Quiz_Model
    fields          = ['post_subject', 'post_content']
    template_name   = "quiz/update_quiz.html"
    post_id = None

    # Validate user is logged in
    def form_valid(self, form):
        form.instance.post_user = self.request.user
        quiz            =   form.save()
        self.quiz_id    =   quiz.post_id
        return super().form_valid(form)

    # Validate user owns post
    def test_func(self):
        isQuizOwner = False
        quiz_detail = self.get_object()
        if self.request.user == quiz_detail.quiz_creator:
            isQuizOwner = True
        return isQuizOwner

    def get_success_url(self):
        return reverse('take_quiz', kwargs={'pk': self.post_id})

class Delete_Quiz(DeleteView):
    model = Quiz_Model
    template_name   = "quiz/delete_quiz.html"

    # Validate user owns post
    def test_func(self):
        isQuizOwner = False
        quiz_detail = self.get_object()
        if self.request.user == quiz_detail.quiz_creator:
            isQuizOwner = True
        return isQuizOwner

    def get_success_url(self):
        return reverse('my_quizzes')

class My_Quizzes(LoginRequiredMixin, ListView):
    model               = Quiz_Model
    ordering            = ['-date']                   # Orders to most recent date
    context_object_name = 'quizzes'
    template_name       = 'quiz/my_quizzes.html'