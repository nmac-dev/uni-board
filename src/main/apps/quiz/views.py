from django.shortcuts           import render, get_object_or_404
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
    paginate_by = 4

class Quiz_Detail(DetailView):
    model = Quiz_Model
    template_name   = "quiz/take_quiz.html"

class Create_Quiz(LoginRequiredMixin, CreateView):
    model           = Quiz_Model
    template_name   = "quiz/create_quiz.html"
    quiz_id         = None
    form_class      = Quiz_Model_Form

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
    template_name   = "quiz/update_quiz.html"
    quiz_id         = None
    form_class      = Quiz_Model_Form

    # Validate user is logged in
    def form_valid(self, form):
        form.instance.creator = self.request.user
        quiz            =   form.save()
        self.quiz_id    =   quiz.quiz_id
        return super().form_valid(form)

    # Validate user owns post
    def test_func(self):
        isQuizOwner = False
        quiz_detail = self.get_object()
        if self.request.user == quiz_detail.creator:
            isQuizOwner = True
        return isQuizOwner

    def get_success_url(self):
        return reverse('take_quiz', kwargs={'pk': self.quiz_id})

class Delete_Quiz(DeleteView):
    model = Quiz_Model
    template_name   = "quiz/delete_quiz_confirm.html"

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
    context_object_name = 'quiz_models'
    template_name       = 'quiz/my_quizzes.html'
    paginate_by = 4


def Quiz_Results(response):
    
    quizTanken = get_object_or_404(Quiz_Model, quiz_id=response.POST.get('quiz_id'))
    answers = response.POST
    print(response.POST)
    print(quizTanken.Question_1_Correct_Answer)

    score = 0
    try:
        if(int(answers.get('q1_opt')) == quizTanken.Question_1_Correct_Answer):
            score +=1
    except:
        pass
    try:
        if(int(answers.get('q2_opt')) == quizTanken.Question_2_Correct_Answer):
            score +=1
    except:
        pass
    try:
        if(int(answers.get('q3_opt')) == quizTanken.Question_3_Correct_Answer):
            score +=1
    except:
        pass
    try:
        if(int(answers.get('q4_opt')) == quizTanken.Question_4_Correct_Answer):
            score +=1
    except:
        pass
    try:
        if(int(answers.get('q5_opt')) == quizTanken.Question_5_Correct_Answer):
            score +=1
    except:
        pass
    try:
        if(int(answers.get('q6_opt')) == quizTanken.Question_6_Correct_Answer):
            score +=1
    except:
        pass
    try:
        if(int(answers.get('q7_opt')) == quizTanken.Question_7_Correct_Answer):
            score +=1
    except:
        pass
    try:
        if(int(answers.get('q8_opt')) == quizTanken.Question_8_Correct_Answer):
            score +=1
    except:
        pass
    try:
        if(int(answers.get('q1_opt')) == quizTanken.Question_9_Correct_Answer):
            score +=1
    except:
        pass
    try:
        if(int(answers.get('q1_opt')) == quizTanken.Question_10_Correct_Answer):
            score +=1
    except:
        pass

    if score == 10:
        message = "Brilliant!"
    elif score > 7:
        message = "Good Job!"

    elif score > 4:
        message = "Not bad!"
    else:
        message = "Better luck next time!"

    args = {}
    args['score'] = score
    args['message'] = message

    return render(response, "quiz/quiz_results.html", args)

