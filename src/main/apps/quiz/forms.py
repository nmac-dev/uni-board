# forms.py
from django import forms
from .models import Quiz_Model

class Quiz_Model_Form(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(Quiz_Model_Form, self).__init__(*args, **kwargs)
        # Required
        self.fields['quiz_title'].required      = True
        self.fields['quiz_desc'].required       = True
        self.fields['quiz_q1_qstn'].required    = True
        self.fields['quiz_q1_opt1'].required    = True
        self.fields['quiz_q1_opt2'].required    = True
        self.fields['quiz_q1_opt3'].required    = True
        self.fields['quiz_q1_opt4'].required    = True
        self.fields['quiz_q1_answer'].required  = True
        # Labels
            # Q1
        self.fields['quiz_q1_qstn'].label   = "Question 1"
        self.fields['quiz_q1_opt1'].label   = "Question 1: Option 1"
        self.fields['quiz_q1_opt2'].label   = "Question 1: Option 2"
        self.fields['quiz_q1_opt3'].label   = "Question 1: Option 3"
        self.fields['quiz_q1_opt4'].label   = "Question 1: Option 4"
        self.fields['quiz_q1_answer'].label = "Question 9: Correct Answer is Option... 1, 2, 3, or 4"
            # Q2
        self.fields['quiz_q2_qstn'].label   = "Question 2"
        self.fields['quiz_q2_opt1'].label   = "Question 2: Option 1"
        self.fields['quiz_q2_opt2'].label   = "Question 2: Option 2"
        self.fields['quiz_q2_opt3'].label   = "Question 2: Option 3"
        self.fields['quiz_q2_opt4'].label   = "Question 2: Option 4"
        self.fields['quiz_q2_answer'].label = "Question 9: Correct Answer is Option... 1, 2, 3, or 4"
            # Q3
        self.fields['quiz_q3_qstn'].label   = "Question 3"
        self.fields['quiz_q3_opt1'].label   = "Question 3: Option 1"
        self.fields['quiz_q3_opt2'].label   = "Question 3: Option 2"
        self.fields['quiz_q3_opt3'].label   = "Question 3: Option 3"
        self.fields['quiz_q3_opt4'].label   = "Question 3: Option 4"
        self.fields['quiz_q3_answer'].label = "Question 9: Correct Answer is Option... 1, 2, 3, or 4"
            # Q4
        self.fields['quiz_q4_qstn'].label   = "Question 4"
        self.fields['quiz_q4_opt1'].label   = "Question 4: Option 1"
        self.fields['quiz_q4_opt2'].label   = "Question 4: Option 2"
        self.fields['quiz_q4_opt3'].label   = "Question 4: Option 3"
        self.fields['quiz_q4_opt4'].label   = "Question 4: Option 4"
        self.fields['quiz_q4_answer'].label = "Question 9: Correct Answer is Option... 1, 2, 3, or 4"
            # Q5
        self.fields['quiz_q5_qstn'].label   = "Question 5"
        self.fields['quiz_q5_opt1'].label   = "Question 5: Option 1"
        self.fields['quiz_q5_opt2'].label   = "Question 5: Option 2"
        self.fields['quiz_q5_opt3'].label   = "Question 5: Option 3"
        self.fields['quiz_q5_opt4'].label   = "Question 5: Option 4"
        self.fields['quiz_q5_answer'].label = "Question 9: Correct Answer is Option... 1, 2, 3, or 4"
            # Q6
        self.fields['quiz_q6_qstn'].label   = "Question 6"
        self.fields['quiz_q6_opt1'].label   = "Question 6: Option 1"
        self.fields['quiz_q6_opt2'].label   = "Question 6: Option 2"
        self.fields['quiz_q6_opt3'].label   = "Question 6: Option 3"
        self.fields['quiz_q6_opt4'].label   = "Question 6: Option 4"
        self.fields['quiz_q6_answer'].label = "Question 9: Correct Answer is Option... 1, 2, 3, or 4"
            # Q7
        self.fields['quiz_q7_qstn'].label   = "Question 7"
        self.fields['quiz_q7_opt1'].label   = "Question 7: Option 1"
        self.fields['quiz_q7_opt2'].label   = "Question 7: Option 2"
        self.fields['quiz_q7_opt3'].label   = "Question 7: Option 3"
        self.fields['quiz_q7_opt4'].label   = "Question 7: Option 4"
        self.fields['quiz_q7_answer'].label = "Question 9: Correct Answer is Option... 1, 2, 3, or 4"
            # Q8
        self.fields['quiz_q8_qstn'].label   = "Question 8"
        self.fields['quiz_q8_opt1'].label   = "Question 8: Option 1"
        self.fields['quiz_q8_opt2'].label   = "Question 8: Option 2"
        self.fields['quiz_q8_opt3'].label   = "Question 8: Option 3"
        self.fields['quiz_q8_opt4'].label   = "Question 8: Option 4"
        self.fields['quiz_q8_answer'].label = "Question 9: Correct Answer is Option... 1, 2, 3, or 4"
            # Q9
        self.fields['quiz_q9_qstn'].label   = "Question 9"
        self.fields['quiz_q9_opt1'].label   = "Question 9: Option 1"
        self.fields['quiz_q9_opt2'].label   = "Question 9: Option 2"
        self.fields['quiz_q9_opt3'].label   = "Question 9: Option 3"
        self.fields['quiz_q9_opt4'].label   = "Question 9: Option 4"
        self.fields['quiz_q9_answer'].label = "Question 9: Correct Answer is Option... 1, 2, 3, or 4"
            # Q10
        self.fields['quiz_q10_qstn'].label   = "Question 10"
        self.fields['quiz_q10_opt1'].label   = "Question 10: Option 1"
        self.fields['quiz_q10_opt2'].label   = "Question 10: Option 2"
        self.fields['quiz_q10_opt3'].label   = "Question 10: Option 3"
        self.fields['quiz_q10_opt4'].label   = "Question 10: Option 4"
        self.fields['quiz_q10_answer'].label = "Question 9: Correct Answer is Option... 1, 2, 3, or 4"

    class Meta:
        model   = Quiz_Model
        exclude = ('quiz_id', 'quiz_creator', 'quiz_date')